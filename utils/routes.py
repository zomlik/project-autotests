from enum import Enum


class ApiRoutes(str, Enum):
    AUTH = "/auth"
    REGISTRY = "auth/register"

    def __str__(self):
        return self.value
