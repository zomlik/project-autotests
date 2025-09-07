import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.link import Link
from locators.navbar_locators import NavBarLocators


class NavbarComponent(BaseComponent):
    locators = NavBarLocators

    def __init__(self, page: Page):
        super().__init__(page)

        self.homepage = Link(page, self.locators.HOMEPAGE_LINK, "Homepage")
        self.projects_link = Link(page, self.locators.PROJECTS_LINK, "Projects")
        self.profile_link = Link(page, self.locators.USER_PROFILE_LINK, "User profile link")

    @allure.step("Клик на лого")
    def click_homepage_logo(self) -> None:
        self.homepage.click()

    @allure.step("Клик на ссылку профиля пользователя")
    def click_user_profile_link(self) -> None:
        self.profile_link.click()
