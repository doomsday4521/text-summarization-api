from pydantic import BaseModel,Field
from fastapi import APIRouter,Request
import logging 
import time
from app.core.config import settings
from app.utils.hashing import hash_text
router = APIRouter(prefix="/summarize",tags=["summarization"])

class SummarizeRequest(BaseModel):
    text:str = Field(
        ...,
        min_length=20,
        max_length=4000,
        description="text to summarize"
    )

class SummarizeResponse(BaseModel):
    summary:str


@router.post("/",response_model=SummarizeResponse)
def summarize(request:SummarizeRequest,req:Request):
    rate_limiter = getattr(req.app.state, "rate_limiter", None)
    if rate_limiter:
        rate_limiter.check(req)
    logger = logging.getLogger("summarize")
    start_time = time.time()
    model =req.app.state.model
    cache = req.app.state.cache
    text_hash = hash_text(request.text)
    cache_key = f"summarize:{text_hash}"
    cached = cache.get(cache_key)
    if cached:
        logger.info("Cache hit")
        return SummarizeResponse(summary=cached)
    
    logger.info("Cache miss, running inference")
    summary  = model.summarize(request.text)
    cache.set(cache_key,summary,ttl=settings.CACHE_TTL)
    logger.info(
        "Summarization completed in %.2f seconds",
        time.time()- start_time
    )
    return SummarizeResponse(
        summary=summary
    )