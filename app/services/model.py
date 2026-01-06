from transformers import pipeline
import logging
logger = logging.getLogger(__name__)
from app.core.config import settings

class SummarizationModel:
    def __init__(self)->None:
        logger.warning("Loading summarization model (this may take time)...")
        self.pipeline = pipeline(
            "summarization",
            model = settings.MODEL_NAME
        )
        logger.warning("Summarization model landed")
    def summarize(self,text:str)->str:
        result  = self.pipeline(
            text,
            max_length=150,
            min_length=40,
            do_sample=False
        )
        return result[0]["summary_text"]