import allure
from httpx import Response

from api.core.api_client import ApiClient
from api.core.public_builder import public_builder
from models.auth.auth_models import AuthNormalRequestModel
from models.auth.user_registry_models import RegistryResponseModel
from utils.url import ApiRoutes


class AuthClient(ApiClient):
    """
    Клиент для работы с /api/v1/auth
    """
    @allure.step("Выполнение запроса на авторизацию")
    def login_api(self, payload: AuthNormalRequestModel) -> Response:
        """
        Метод выполняет авторизацию пользователя по username и password
        :param payload: Данные для авторизации
        :return: Объект Response с данными ответа
        """
        return self.post(ApiRoutes.AUTH, json=payload.model_dump(by_alias=True))

    @allure.step("Получение JSON-ответа после авторизации")
    def login(self, payload: AuthNormalRequestModel) -> RegistryResponseModel:
        """
        Метод выполняет запрос на авторизацию и возвращает ответ
        :param payload: Данные пользователя
        :return: Объект AuthResponseModel с данными ответа
        """
        response = self.login_api(payload)
        return RegistryResponseModel.model_validate_json(response.text)


def auth_client() -> AuthClient:
    return AuthClient(client=public_builder())
