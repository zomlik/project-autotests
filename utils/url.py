from enum import Enum


class Url(str, Enum):
    AUTH = "./login"
    PROFILE = "./profile"

    def __str__(self):
        return self.value


class ApiRoutes(str, Enum):
    AUTH = "/auth"
    REFRESH_TOKEN = "/auth/refresh"
    REGISTRY = "auth/register"
    USERS = "/users"

    def __str__(self):
        return self.value
