import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage


def test_valid_login_to_orangehrm(page: Page):
    login_page = LoginPage(page)
    login_page.login_with_valid_admin()


@pytest.mark.parametrize(
    "username, password",
    [
        ("admin", "0000"),  # wrong passwrod
        ("peter", "admin123"),  # wrong username
        ("jjfdf", "iohrfsdf"),  # both
        ("مالك", "iohrfsdf"),  # both
    ],
)
def test_invalid_creds(page: Page, username, password):
    login_page = LoginPage(page)
    login_page.invalid_login(username=username, password=password)
