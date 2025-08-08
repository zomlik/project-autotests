import allure
import pytest

from utils.allure_constants import Feature
from utils.url import Url


@allure.feature(Feature.AUTH)
@pytest.mark.ui
@pytest.mark.user
@pytest.mark.smoke
class TestAuth:

    @allure.title("ID-94: Авторизация пользователя с валидными данными")
    def test_auth_new_user(self, create_new_user, login_page):
        login_page.open(Url.AUTH)
        login_page.fill_login_form(
            login=create_new_user.email,
            password=create_new_user.password
        )
        login_page.click_login_button()
        login_page.nav_bar.click_user_profile_link()
        login_page.check_current_url(Url.PROFILE)
