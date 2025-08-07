from typing import Pattern

import allure
from playwright.sync_api import Page, Response, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открыть страницу {url}")
    def open(self, url: str) -> Response | None:
        return self.page.goto(url, wait_until="networkidle")

    @allure.step("Перезагрузить страницу")
    def reload(self) -> Response | None:
        return self.page.reload(wait_until="domcontentloaded")

    @allure.step("Проверка текущего url")
    def check_current_url(self, expected_url: Pattern[str]):
        expect(self.page).to_have_url(expected_url)
