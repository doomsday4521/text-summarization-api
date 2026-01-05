from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    APP_NAME:str = "Text summarization api"
    DEBUG:bool = True
    REDIS_URL:str = "redis://localhost:6379/0"
    CACHE_TTL:int = 300
    class Config:
        env_file = ".env"


settings = Settings()