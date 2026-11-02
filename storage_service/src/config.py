"""Configuration for the storage service."""

from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Настройка: читать переменные с префиксом APP_ из файла .env
    model_config = SettingsConfigDict(env_prefix="APP_", env_file=".env")
    
    port: int = 8001
    log_level: str = "INFO"


@lru_cache
def get_settings() -> Settings:
    """Return cached settings (singleton)."""
    return Settings() # type: ignore