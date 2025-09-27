import allure
from httpx import Response

from api.core.api_client import ApiClient
from api.core.private_builder import private_builder
from models.auth.auth_models import UserAuthData
from models.webhooks.webhooks_models import CreateWebhooksRequestModel
from utils.url import ApiRoutes


class WebhooksClient(ApiClient):

    @allure.step("Получить списка Webhooks")
    def get_webhooks_list(self, project: int | None = None) -> Response:
        """
        Метод получение списка WebHooks
        :param project: id проекта
        :return: Объект Response с данными ответа
        """
        return self.get(ApiRoutes.WEBHOOKS, params={"project": project})

    @allure.step("Создание нового webhook")
    def create_webhooks(self, payload: CreateWebhooksRequestModel) -> Response:
        """
        Метод создает новый webhook
        :param payload: Данные для создания webhook
        :return: Объект Response с данными ответа
        """
        return self.post(ApiRoutes.WEBHOOKS, json=payload.model_dump(by_alias=True))


def webhooks_client(user_data: UserAuthData) -> WebhooksClient:
    return WebhooksClient(client=private_builder(user_data))
