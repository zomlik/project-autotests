from typing import Any

import allure
from httpx import URL, Client, QueryParams, Response


class ApiClient:
    def __init__(self, client: Client):
        """
        Базовый API клиент, принимающий объект httpx.Client.

        :param client: экземпляр httpx.Client для выполнения HTTP-запросов
        """
        self.client = client

    @allure.step("Выполнение GET-Запроса")
    def get(self, url: URL | str, params: dict[str, Any] | None = None) -> Response:
        """
        Выполняет GET-запрос.

        :param url: URL-адрес для запроса
        :param params: Параметры запроса (query parameters)
        :return: Объект Response с данными ответа
        """
        params = {k: v for k, v in (params or {}).items() if v is not None}
        return self.client.get(url, params=QueryParams(params))

    @allure.step("Выполнение POST-Запроса")
    def post(self, url: str, json: Any | None = None) -> Response:
        """
        Выполняет POST-запрос.

        :param url: URL-адрес для запроса
        :param json: Данные в формате JSON
        :return: Объект Response с данными ответа
        """
        return self.client.post(url, json=json)

    @allure.step("Выполнение PUT-Запроса")
    def put(self, url: str, json: Any | None = None) -> Response:
        """
        Выполняет PUT-запрос.

        :param url: URL-адрес для запроса
        :param json: Данные в формате JSON
        :return: Объект Response с данными ответа
        """
        return self.client.put(url, json=json)

    @allure.step("Выполнение PATCH-Запроса")
    def patch(self, url: str, json: Any | None = None) -> Response:
        """
        Выполняет PATHC-запрос.

        :param url: URL-адрес для запроса
        :param json: Данные в формате JSON
        :return: Объект Response с данными ответа
        """
        return self.client.patch(url, json=json)

    @allure.step("Выполнение DELETE-Запроса")
    def delete(self, url: str) -> Response:
        """
        Выполняет DELETE-запрос.

        :param url: URL-адрес для запроса
        :return: Объект Response с данными ответа
        """
        return self.client.delete(url)
