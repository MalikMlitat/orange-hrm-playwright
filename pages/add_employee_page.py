from playwright.sync_api import Page


class AddEmployeePage:

    def __init__(self, page: Page):
        self.page = page
        self.add_employee_link = page.get_by_role("link", name="Add Employee")
        self.first_name = page.get_by_role("textbox", name="First Name")
        self.middle_name = page.get_by_role("textbox", name="Middle Name")
        self.last_name = page.get_by_role("textbox", name="Last Name")
        self.save_button = page.get_by_role("button", name="Save")

    def add_employee(self, first, middle, last):
        self.add_employee_link.click()
        self.first_name.fill(first)
        self.middle_name.fill(middle)
        self.last_name.fill(last)
        self.save_button.click()