from enum import Enum


class Url(str, Enum):
    AUTH = "./login"
    PROFILE = "./profile"
    REGISTER = "./register"
    PROJECTS = "./projects"
    CREATE_SCRUM_PROJECT = "./project/new/scrum"

    def __str__(self):
        return self.value


class ApiRoutes(str, Enum):
    AUTH = "/auth"
    REFRESH_TOKEN = "/auth/refresh"
    REGISTRY = "auth/register"
    USERS = "/users"
    WEBHOOKS = "/webhooks"

    def __str__(self):
        return self.value
