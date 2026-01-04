from fastapi import FastAPI
from app.core.config import settings
from app.api.summarize import router as summarize_router

def create_app()->FastAPI:
    app = FastAPI(title=settings.APP_NAME)

    app.include_router(summarize_router)

    @app.get("/health")
    def health_check():
        return {"status":"ok"}
    
    return app

app = create_app()