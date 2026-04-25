import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage

pytest_plugins = ["tests.api_fixture"]


@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getini("base_url")


@pytest.fixture(scope="function", autouse=True)
def goto(page: Page):
    """Fixture to navigate to the base URL."""
    page.goto("/")


@pytest.fixture
def login_with_admin(page: Page):
    LoginPage(page).login_with_valid_admin()
