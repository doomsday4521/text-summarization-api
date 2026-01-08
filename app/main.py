from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from app.core.exception_handlers import validation_exception_handler
from app.core.exception_handlers import internal_exception_handler
from app.core.config import settings
import logging
from app.services.rate_limiter import RateLimiter
import time
from app.core.logging import setup_logging
from app.api.summarize import router as summarize_router
from app.services.model import SummarizationModel
from app.services.cache import CacheService
def create_app()->FastAPI:
    setup_logging()
    logger = logging.getLogger("app")
    app = FastAPI(title=settings.APP_NAME)
    logger.info("Application startup")
    app.add_exception_handler(
        RequestValidationError,
        validation_exception_handler
    )
    app.add_exception_handler(
        Exception,
        internal_exception_handler
    )
    start_time = time.time()
    app.state.model = SummarizationModel()
    logger.info(
        "Model loaded in %.2f seconds",
        time.time() - start_time
    )
    app.state.cache = CacheService(settings.REDIS_URL)
    app.state.rate_limiter =None
    logger.info("Cache initialized")
    app.include_router(summarize_router)

    @app.get("/health")
    def health_check():
        return {"status":"ok"}
    
    return app

app = create_app()