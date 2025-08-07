import allure
from playwright.sync_api import Page, expect

from elements.button import Button
from elements.link import Link
from locators.login_page_locators import LoginPageLocator
from pages.base_page import BasePage


class LoginPage(BasePage):
    locator = LoginPageLocator()

    def __init__(self, page: Page):
        super().__init__(page)

        self.login_button = Button(page, self.locator.LOGIN_BUTTON, "Login")
        self.create_account_link = Link(page, self.locator.CREATE_ACCOUNT_LINK, "Create Account Link")

    @allure.step("Заполнить форму логина")
    def fill_login_form(self, login: str, password: str) -> None:
        self.page.locator(self.locator.USERNAME_FIELD).fill(login)
        expect(self.page.locator(self.locator.USERNAME_FIELD)).to_have_value(login)

        self.page.locator(self.locator.PASSWORD_FIELD).fill(password)
        expect(self.page.locator(self.locator.PASSWORD_FIELD)).to_have_value(password)

    @allure.step("Кликнуть на кнопку логина")
    def click_login_button(self) -> None:
        self.login_button.click()

    @allure.step("Кликнуть на ссылку 'Create account link'")
    def click_create_account_link(self) -> None:
        self.create_account_link.click()
