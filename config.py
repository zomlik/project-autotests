from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class HttpClientConfig(BaseModel):
    base_url: str
    timeout: float


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent / ".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="."
    )
    http_client: HttpClientConfig


settings = Settings()
