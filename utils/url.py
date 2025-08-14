from enum import Enum

from config import settings


class Url(str, Enum):
    _BASE_URL = settings.playwright.base_url
    AUTH = f"{_BASE_URL}/login"
    PROFILE = f"{_BASE_URL}/profile"

    def __str__(self):
        return self.value


class ApiRoutes(str, Enum):
    AUTH = "/auth"
    REFRESH_TOKEN = "/auth/refresh"
    REGISTRY = "auth/register"
    USERS = "/users"

    def __str__(self):
        return self.value
