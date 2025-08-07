import pytest

from pages.login_page import LoginPage


@pytest.fixture()
def login_page(browser) -> LoginPage:
    return LoginPage(page=browser)
