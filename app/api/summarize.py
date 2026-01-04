from pydantic import BaseModel,Field
from fastapi import APIRouter,Request

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
    summary  = model.summarize(request.text)
    return SummarizeResponse(
        summary=summary
    )