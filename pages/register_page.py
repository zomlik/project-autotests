import allure
from playwright.sync_api import Page, expect

from components.navbar_component import NavbarComponent
from elements.input import Input
from elements.link import Link
from elements.text import Text
from locators.register_page_locators import RegisterPageLocators
from pages.base_page import BasePage


class RegisterPage(BasePage):
    """"Класс, представляющий страницу регистрации в системе"""
    locator = RegisterPageLocators()

    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)

        self.username_field = Input(page, self.locator.USERNAME_FIELD, "Username")
        self.full_name_field = Input(page, self.locator.FULL_NAME_FIELD, "Full Name")
        self.email_filed = Input(page, self.locator.EMAIL_FIELD, "Email")
        self.password_field = Input(page, self.locator.PASSWORD_FIELD, "Password")

        self.sing_up_button = Input(page, self.locator.SING_UP_BUTTON, "Sing Up")
        self.log_in_link = Link(page, self.locator.LOGIN_IN_LINK, "Log in")

        self.password_field_errors = Text(page, self.locator.USERNAME_FIELD_ERROR, "Password Error")

    @allure.step("Заполнить форму регистрации")
    def fill_register_form(self,
                           username: str | None,
                           full_name: str | None,
                           email: str | None,
                           password: str | None) -> None:
        self.username_field.fill(username)
        expect(self.page.locator(self.locator.USERNAME_FIELD)).to_have_value(username)

        self.full_name_field.fill(full_name)
        expect(self.page.locator(self.locator.FULL_NAME_FIELD)).to_have_value(full_name)

        self.email_filed.fill(email)
        expect(self.page.locator(self.locator.EMAIL_FIELD)).to_have_value(email)

        self.password_field.fill(password)
        expect(self.page.locator(self.locator.PASSWORD_FIELD)).to_have_value(password)

    @allure.step("Клик на кнопку регистрации")
    def click_sing_up_button(self) -> None:
        self.sing_up_button.click()

    @allure.step("Клик на ссылку авторизации")
    def click_log_in_link(self) -> None:
        self.log_in_link.click()

    @allure.step("Текст ошибки поля username соответствует {expected_text}")
    def check_username_error(self, expected_text: str) -> None:
        expect(self.page.locator(self.locator.USERNAME_FIELD_ERROR)).to_have_text(expected_text)

    @allure.step("Текст ошибки поля password соответствует {expected_text}")
    def check_password_error(self, expected_text: str) -> None:
        expect(self.page.locator(self.locator.PASSWORD_FIELD_ERROR)).to_have_text(expected_text)
