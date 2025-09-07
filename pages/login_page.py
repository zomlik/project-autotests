import allure
from playwright.sync_api import Page, expect

from components.navbar_component import NavbarComponent
from elements.button import Button
from elements.input import Input
from elements.link import Link
from locators.login_page_locators import LoginPageLocator
from pages.base_page import BasePage


class LoginPage(BasePage):
    """"Класс, представляющий страницу логина в системе"""
    locator = LoginPageLocator()

    def __init__(self, page: Page):
        super().__init__(page)

        self.username_field = Input(page, self.locator.USERNAME_FIELD, "Username")
        self.password_field = Input(page, self.locator.PASSWORD_FIELD, "Password")
        self.login_button = Button(page, self.locator.LOGIN_BUTTON, "Login")
        self.create_account_link = Link(page, self.locator.CREATE_ACCOUNT_LINK, "Create Account Link")
        self.nav_bar = NavbarComponent(page)

    @allure.step("Заполнить форму логина")
    def fill_login_form(self, login: str, password: str) -> None:
        """
        Метод заполняет форму логина
        :param login:
        :param password:
        :return:
        """
        self.username_field.fill(login)
        expect(self.page.locator(self.locator.USERNAME_FIELD)).to_have_value(login)

        self.password_field.fill(password)
        expect(self.page.locator(self.locator.PASSWORD_FIELD)).to_have_value(password)

    @allure.step("Кликнуть на кнопку Log in")
    def click_login_button(self) -> None:
        """Метод кликает на кнопку авторизации"""
        self.login_button.click()

    @allure.step("Кликнуть на ссылку 'Create account link'")
    def click_create_account_link(self) -> None:
        """Метод кликает на ссылку создания нового аккаунта"""
        self.create_account_link.click()
