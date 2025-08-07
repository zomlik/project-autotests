from playwright.sync_api import expect

from elements.base_element import BaseElement


class Input(BaseElement):
    @property
    def type_of(self) -> str:
        return "input"

    def fill(self, value: str, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        locator.fill(value)

    def check_have_value(self, value: str, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_value(value)
