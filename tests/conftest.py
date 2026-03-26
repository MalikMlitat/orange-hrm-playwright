import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.fixture(scope="function", autouse=True)
def goto(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@pytest.fixture
def login_with_admin(page: Page):
    LoginPage(page).login_with_valid_admin()