"""Configuration for the gateway service."""

from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    model_config = SettingsConfigDict(env_prefix="APP_", env_file=".env")
    
    port: int = 8000
    storage_url: str = "http://127.0.0.1:8001"
    timeout: float = 5.0


@lru_cache
def get_settings() -> Settings:
    """Return cached settings (singleton)."""
    return Settings() # type: ignore