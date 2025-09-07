from enum import Enum


class Epic(str, Enum):
    USERS = "Пользователи"


class Feature(str, Enum):
    AUTH = "Auth"
    REGISTER = "Register"
    USER = "User"

    def __str__(self):
        return self.value


class Tag(str, Enum):
    API = "API"
    UI = "UI"

    def __str__(self):
        return self.value
