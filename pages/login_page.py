from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self, username, password):
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def login_with_valid_admin(self):
        self.login("admin", "admin123")
        self.verify_login_ok()

    def invalid_login(self, username, password):
        self.login(username, password)
        expect(self.page.get_by_text("Invalid credentials")).to_be_visible()

    def verify_login_ok(self):
        dashboard_title = self.page.get_by_role("heading", name="Dashboard")
        expect(dashboard_title).to_be_visible(timeout=60000)
