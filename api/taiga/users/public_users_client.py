import allure
from httpx import Response

from api.core.api_client import ApiClient
from api.core.public_builder import public_builder
from models.auth.auth_model import AuthNormalRequestModel
from models.auth.user_registry import PublicRegistryRequestModel
from utils.url import ApiRoutes


class PublicUsersClient(ApiClient):
    """
        Клиент для работы с /api/v1/auth/register
    """
    @allure.step("Выполнение авторизации пользователя")
    def auth(self, user_data: AuthNormalRequestModel) -> Response:
        return self.post(ApiRoutes.AUTH, json=user_data.model_dump(by_alias=True))

    @allure.step("Выполнение публичной регистрации пользователя")
    def create_public_user(self, payload: PublicRegistryRequestModel):
        return self.post(ApiRoutes.REGISTRY, json=payload.model_dump(by_alias=True))


def public_users_client() -> PublicUsersClient:
    return PublicUsersClient(client=public_builder())
