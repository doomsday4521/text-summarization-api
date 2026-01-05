from pydantic import BaseModel,Field
from fastapi import APIRouter,Request
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
    model =req.app.state.model
    cache = req.app.state.cache
    text_hash = hash_text(request.text)
    cache_key = f"summarize:{text_hash}"
    cached = cache.get(cache_key)
    if cached:
        return SummarizeResponse(summary=cached)
    summary  = model.summarize(request.text)
    cache.set(cache_key,summary,ttl=300)
    return SummarizeResponse(
        summary=summary
    )