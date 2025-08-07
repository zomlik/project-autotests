from enum import Enum

from config import settings


class Url(str, Enum):
    _BASE_URL = settings.playwright.base_url
    AUTH = f"{_BASE_URL}/login"

    def __str__(self):
        return self.value


class ApiRoutes(str, Enum):
    AUTH = "/auth"
    REGISTRY = "auth/register"

    def __str__(self):
        return self.value
