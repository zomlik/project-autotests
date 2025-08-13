import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement


class Input(BaseElement):
    """Класс для работы с элементами input (полями ввода) на веб-странице"""

    @property
    def type_of(self) -> str:
        return "input"

    def fill(self, value: str, **kwargs) -> None:
        """
        Заполняет поле ввода указанным значением.
        :param value: Значение, которое нужно ввести в поле
        :param kwargs: Дополнительные аргументы для локатора
        """
        locator = self.get_locator(**kwargs)
        with allure.step(f"Заполнить поле {self.name} значением {value}"):
            locator.fill(value)

    def check_have_value(self, value: str, **kwargs) -> None:
        """
        Проверяет, что поле ввода содержит указанное значение
        :param value: Ожидаемое значение в поле ввода
        :param kwargs: Дополнительные аргументы для локатора
        :return: AssertionError: Если поле не содержит указанное значение
        """
        locator = self.get_locator(**kwargs)
        with allure.step(f"Проверка, что значение {value} есть в поле {self.name}"):
            expect(locator).to_have_value(value)

    def press_enter(self, **kwargs) -> None:
        """
        Нажимает клавишу Enter в поле ввода.
        :param kwargs: Дополнительные аргументы для локатора
        """
        locator = self.get_locator(**kwargs)
        with allure.step(f"Нажатие кнопки Enter для поля {self.name}"):
            locator.press("Enter")
