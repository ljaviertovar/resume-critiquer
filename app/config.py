"""Application configuration using pydantic-settings for environment validation."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from .env file with runtime validation."""

    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"
    max_tokens: int = 1500
    temperature: float = 0.7

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


# Singleton instance - raises ValidationError if required env vars are missing
settings = Settings()
