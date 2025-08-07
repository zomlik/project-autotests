import pytest
from playwright.sync_api import Page, Playwright

from config import settings


@pytest.fixture()
def browser(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=settings.playwright.headless,
                                         args=["--ignore-certificate-errors"])
    yield browser.new_page()
    browser.close()
