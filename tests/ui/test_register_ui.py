import allure
import pytest

from utils.allure_constants import Feature
from utils.fake_data import fake
from utils.url import Url


@allure.feature(Feature.REGISTER)
@pytest.mark.ui
@pytest.mark.users
@pytest.mark.registry
class TestRegister:

    @allure.title("Регистрация пользователя с недопустимыми символами в поле username")
    @pytest.mark.regression
    def test_invalid_value_in_username_field(self, register_page):
        register_page.open(Url.REGISTER)
        register_page.fill_register_form(
            username="@name",
            full_name=fake.full_name(),
            email=fake.email(),
            password=fake.password()
        )
        register_page.click_sing_up_button()
        register_page.check_username_error("This value seems to be invalid.")

    @allure.title("Регистрация пользователя с паролем из 6 знаков")
    @pytest.mark.regression
    def test_register_with_min_password_length(self, register_page):
        register_page.open(Url.REGISTER)
        register_page.fill_register_form(
            username=fake.username(),
            full_name=fake.full_name(),
            email=fake.email(),
            password="123456"
        )
        register_page.click_sing_up_button()
        register_page.navbar.click_user_profile_link()
        register_page.check_current_url(Url.PROFILE)

    @allure.title("Регистрация пользователя с паролем из 5 знаков")
    @pytest.mark.regression
    def test_invalid_password_length(self, register_page):
        register_page.open(Url.REGISTER)
        register_page.fill_register_form(
            username=fake.username(),
            full_name=fake.full_name(),
            email=fake.email(),
            password="12345"
        )
        register_page.click_sing_up_button()
        register_page.check_password_error("Ensure this value has at least"
                                           " 6 characters (it has 5).")
