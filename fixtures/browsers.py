import pytest
from playwright.sync_api import Browser, BrowserContext, Page

from config import settings


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """
    Фикстура для настройки параметров запуска браузера.
    :param browser_type_launch_args: Стандартные аргументы запуска браузера от Playwright
    :return: Обновлённые аргументы запуска с настройками из конфига
    """
    return {
        **browser_type_launch_args,
        "headless": settings.playwright.headless,
    }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Фикстура для настройки контекста браузера
    :param browser_context_args: Стандартные аргументы контекста браузера от Playwright
    :return: Обновлённые аргументы контекста с заданными настройками
    """
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True,
    }


@pytest.fixture()
def get_browser(browser: Browser, browser_context_args: dict) -> Page:
    """
    Основная фикстура для тестов, предоставляющая готовую страницу браузера
    :param browser: Экземпляр браузера из фикстуры pytest-playwright
    :param browser_context_args: Аргументы контекста браузера
    :return: Готовая к использованию страница браузера с настроенным контекстом
    """
    context = browser.new_context(
        **browser_context_args,
        base_url=settings.get_base_url()
    )
    page = context.new_page()
    yield page
    context.close()
