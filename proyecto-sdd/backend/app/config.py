import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "9524 API"
    VERSION: str = "0.1.0"
    CORS_ORIGINS: str = "http://localhost:5171,http://localhost:5172,http://localhost:5173,http://127.0.0.1:5171,http://127.0.0.1:5172,http://127.0.0.1:5173"
    DATABASE_URL: str = "sqlite:///./app.db"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()

# Normalización para Render (si viene postgres:// convertir a postgresql://)
db_url = os.getenv("DATABASE_URL", settings.DATABASE_URL)
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

SETTINGS_DATABASE_URL = db_url
