import allure
from httpx import Response

from api.core.api_client import ApiClient
from api.core.public_builder import public_builder
from api.taiga.auth.auth_client import auth_client
from models.auth.auth_models import (
    AuthNormalRequestModel,
    RefreshTokenRequestModel,
    UserAuthData,
)
from models.auth.user_registry_models import PublicRegistryRequestModel
from utils.url import ApiRoutes


class PublicUsersClient(ApiClient):
    """
        Клиент для работы с /api/v1/auth/register
    """
    @allure.step("Выполнение авторизации пользователя")
    def auth(self, user_data: UserAuthData) -> Response:
        request_data = AuthNormalRequestModel(username=user_data.username or user_data.email,
                                              password=user_data.password,
                                              type=user_data.type
                                              )
        response = auth_client().login_api(request_data)
        return response

    @allure.step("Выполнение публичной регистрации пользователя")
    def create_public_user(self, payload: PublicRegistryRequestModel):
        return self.post(ApiRoutes.REGISTRY, json=payload.model_dump(by_alias=True))

    @allure.step("Обновление токена")
    def refresh_token(self, user_data: UserAuthData) -> Response:
        """
        Метод выполняет запрос на обновление токена
        :param user_data: Данные для авторизации
        :return: Объект Response с данными ответа
        """
        auth_response = auth_client().login(user_data)
        token_data = RefreshTokenRequestModel(refresh=auth_response.auth_token)
        return self.post(ApiRoutes.REFRESH_TOKEN, json=token_data.model_dump(by_alias=True))


def public_users_client() -> PublicUsersClient:
    return PublicUsersClient(client=public_builder())
