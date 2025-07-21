from enum import Enum


class ApiRoutes(str, Enum):
    AUTH = "/auth"

    def __str__(self):
        return self.value
