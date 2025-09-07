import pytest

from pages.login_page import LoginPage
from pages.register_page import RegisterPage


@pytest.fixture()
def login_page(get_browser) -> LoginPage:
    return LoginPage(page=get_browser)


@pytest.fixture()
def register_page(get_browser) -> RegisterPage:
    return RegisterPage(page=get_browser)
