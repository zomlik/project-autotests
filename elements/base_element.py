from abc import ABC, abstractmethod

import allure
from playwright.sync_api import Locator, Page, expect


class BaseElement(ABC):
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.locator = locator
        self.name = name

    @property
    @abstractmethod
    def type_of(self) -> str:
        return "base element"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        with allure.step(f"Получение локатора {locator} с индексом {nth}"):
            return self.page.locator(locator).nth(nth)

    def click(self, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        with allure.step(f"Клик на {self.type_of} '{self.name}'"):
            locator.click()

    def check_visible(self, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        with allure.step(f"Проверка, что {self.type_of} '{self.name}' отображается на странице"):
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        with allure.step(f"Проверка, что {self.type_of} '{self.name}' есть текст {text}"):
            expect(locator).to_have_text(text)
