from pathlib import Path

from pydantic import BaseModel, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class HttpClientConfig(BaseModel):
    base_url: str
    timeout: float


class PlaywrightConfig(BaseModel):
    base_url: str
    headless: bool
    viewport_wight: int | None = None
    viewport_height: int | None = None


class User(BaseModel):
    username: str
    email: str
    password: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent / ".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="."
    )
    http_client: HttpClientConfig
    playwright: PlaywrightConfig
    browser_state_file: FilePath
    super_user: User

    def get_base_url(self) -> str:
        return self.playwright.base_url


settings = Settings.initialize()
