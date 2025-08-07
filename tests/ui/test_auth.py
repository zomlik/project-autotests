import allure
import pytest

from utils.allure_constants import Feature
from utils.url import Url


@allure.feature(Feature.AUTH)
@pytest.mark.ui
@pytest.mark.user
@pytest.mark.smoke
class TestAuth:
    @allure.title("Авторизация пользователя с не верными данными")
    @allure.testcase("")
    def test_auth_user(self, login_page):
        login_page.open(Url.AUTH)
        login_page.fill_login_form(login="login", password="password")
        login_page.click_login_button()
