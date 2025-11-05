from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "AI Interview Platform"
    API_V1_PREFIX: str = "/api/v1"
    ENV: str = "dev"
    DEBUG: bool = True
    # DATABASE_URL: str = "postgresql+asyncpg://user:pass@db:5432/ai_interviews"
    # REDIS_URL: str = "redis://redis:6379/0"

    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    return Settings()
