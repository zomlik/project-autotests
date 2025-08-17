import allure
import pytest

from utils.allure_constants import Feature
from utils.url import Url


@allure.feature(Feature.AUTH)
@pytest.mark.ui
@pytest.mark.users
@pytest.mark.smoke
class TestAuth:

    @allure.title("Авторизация пользователя с валидными данными")
    def test_auth_new_user(self, get_user_session, login_page):
        login_page.open(Url.AUTH)
        login_page.fill_login_form(
            login=get_user_session.auth.email,
            password=get_user_session.auth.password
        )
        login_page.click_login_button()
        login_page.nav_bar.click_user_profile_link()
        login_page.check_current_url(Url.PROFILE)
