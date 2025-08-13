import pytest
from playwright.sync_api import Page, Playwright

from config import settings


def initialize_playwright(
        playwright: Playwright,
        storage_state: str | None = None
) -> Page:
    browser = playwright.chromium.launch(
        headless=settings.playwright.headless,
        args=["--ignore-certificate-errors"],
    )
    context = browser.new_context(storage_state=storage_state)
    yield context.new_page()
    browser.close()


@pytest.fixture()
def browser(playwright: Playwright) -> Page:
    yield from initialize_playwright(playwright)
