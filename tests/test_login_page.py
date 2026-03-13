import pytest

from pages.login_page import LoginPage


class TestLoginPage:
    def test_valid_login(self, page):
        login = LoginPage(page)
        login.navigate()
        login.valid_login("Admin", "admin123")

    @pytest.mark.parametrize(
        ("username", "password"),
        [("Admin", "wrongpassword"), ("wronguser", "admin123"), ("wronguser", "wrongpassword")],
    )
    def test_invalid_login(self, page, username, password):
        login = LoginPage(page)
        login.navigate()
        login.invalid_login(username=username, password=password)
