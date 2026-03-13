"""Login page object."""

from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("input[name='username']")
        self.password = page.locator("input[name='password']")
        self.login_button = page.locator("button[type='submit']")

    def navigate(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/")

    def login(self, username: str, password: str):
        """Login to system."""
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
        self.page.wait_for_timeout(5000)  # Wait for 5 seconds to ensure the page has loaded

    def valid_login(self, username: str, password: str):
        """Login with valid credentials."""
        self.login(username, password)
        expect(self.page.get_by_role("heading", name="Dashboard")).to_be_visible()

    def invalid_login(self, username: str, password: str):
        """Login with invalid credentials."""
        self.login(username, password)
        expect(self.page.get_by_text("Invalid credentials")).to_be_visible()
