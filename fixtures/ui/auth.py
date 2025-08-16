import pytest

from pages.login_page import LoginPage


@pytest.fixture()
def login_page(get_browser) -> LoginPage:
    return LoginPage(page=get_browser)
