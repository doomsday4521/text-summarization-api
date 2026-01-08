from pydantic_settings import BaseSettings
from pydantic import ConfigDict
class Settings(BaseSettings):
    APP_NAME:str = "Text summarization api"
    DEBUG:bool = True
    MODEL_NAME: str = "facebook/bart-large-cnn"
    SUMMARY_MAX_LEN: int = 150
    REDIS_URL:str = "redis://localhost:6379/0"
    CACHE_TTL:int = 300
    model_config = ConfigDict(
        env_file=".env"
    )


settings = Settings()