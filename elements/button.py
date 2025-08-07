import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement


class Button(BaseElement):
    @property
    def type_of(self) -> str:
        return "button"

    def check_enabled(self, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        with allure.step(f"Проверка, что элемент {self.type_of} '{self.name}' активен"):
            expect(locator).to_be_enabled()

    def check_disabled(self, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        with allure.step(f"Проверка, что элемент {self.type_of} '{self.name}' не активен"):
            expect(locator).to_be_disabled()
