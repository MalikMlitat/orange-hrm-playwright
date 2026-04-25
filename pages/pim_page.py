from playwright.sync_api import Page, expect

from pages.pim.add_employee_page import AddEmployeePage


class PimPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.get_by_text("PIM", exact=True).click()
        expect(self.page.get_by_role("heading", name="PIM")).to_be_visible()

    def visit_tab_add_employee(self):
        self.page.get_by_text("Add Employee").click()
        expect(self.page.get_by_role("heading", name="Add Employee")).to_be_visible()

        return AddEmployeePage(self.page)

    def visit_tab_employee_list(self):
        self.page.get_by_text("Employee List").click()
        expect(self.page.get_by_role("heading", name="Employee List")).to_be_visible()

        # return EmployeeListPage(self.page)
