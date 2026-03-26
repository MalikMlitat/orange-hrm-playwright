import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

def test_valid_login_to_orangehrm(page: Page):
    login_page = LoginPage(page)
    login_page.login_with_valid_admin()

def test_invalid_password_login(page: Page):
    login_page = LoginPage(page)
    login_page.invalid_login(username="Admin", password="0000")

def test_invalid_user_login(page: Page):
    login_page = LoginPage(page)
    login_page.invalid_login(username="peter", password="admin123")

@pytest.mark.parametrize("username, password", [
    ("Admin", "0000"),
    ("peter", "admin123"),
    ("qwer", "tyui"),
])
def test_invalid_creds(page: Page, username, password):
    login_page = LoginPage(page)
    login_page.invalid_login(username=username, password=password)