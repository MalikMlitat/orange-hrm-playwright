"""Employee page object."""

from playwright.sync_api import Page


class EmployeePage:
    def __init__(self, page: Page):
        self.page = page

    def open_pim(self):
        """Navigate to PIM section."""
        self.page.click("text=PIM")

    def click_add_employee(self):
        """Open add employee form."""
        self.page.click("text=Add Employee")

    def add_employee_without_login(self, first, last):
        """Add employee without login details."""
        self.page.fill("input[name='firstName']", first)
        self.page.fill("input[name='lastName']", last)
        self.page.click("button[type='submit']")

    def add_employee_with_login(self, first, last, username, password):
        self.page.fill("input[name='firstName']", first)
        self.page.fill("input[name='lastName']", last)

        # activate login details
        self.page.locator(".oxd-switch-input").click()

        # login fields
        self.page.locator('input[autocomplete="off"]').nth(0).fill(username)
        self.page.locator('input[type="password"]').nth(0).fill(password)
        self.page.locator('input[type="password"]').nth(1).fill(password)

        self.page.get_by_role("button", name="Save").click()
