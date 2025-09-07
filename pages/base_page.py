from typing import Pattern

import allure
from playwright.sync_api import Page, Response, expect


class BasePage:
    """Базовый класс для всех страниц, предоставляющий общие методы работы с веб-страницей."""

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открыть страницу {url}")
    def open(self, url: str) -> Response | None:
        """
        Открывает указанный URL в браузере
        :param url: URL страницы для открытия
        :return: Объект ответа сервера или None
        """
        return self.page.goto(url, wait_until="networkidle")

    @allure.step("Перезагрузить страницу")
    def reload(self) -> Response | None:
        """
        Перезагружает текущую страницу
        :return: Объект ответа сервера или None
        """
        return self.page.reload(wait_until="domcontentloaded")

    @allure.step("Проверка текущего url")
    def check_current_url(self, expected_url: Pattern[str] | str) -> None:
        """
        Проверяет, что текущий URL соответствует ожидаемому
        :param expected_url: Ожидаемый URL (может быть строкой или регулярным выражением)
        :raise: AssertionError: Если текущий URL не соответствует ожидаемому
        """
        expect(self.page).to_have_url(expected_url)
