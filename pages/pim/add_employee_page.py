from playwright.sync_api import Page, expect

from data.Employee import Employee


class AddEmployeePage:
    def __init__(self, page: Page):
        self.page = page

    def add_employee_without_details(self, employee: Employee = None):
        if employee is None:
            employee = Employee()

        if employee.pic_path:
            self.page.locator('input[type="file"]').set_input_files(employee.pic_path)
            self.page.wait_for_timeout(5000)
        self.page.get_by_placeholder("First Name").fill(employee.first)
        self.page.get_by_placeholder("Middle Name").fill(employee.middle)
        self.page.get_by_placeholder("Last Name").fill(employee.last)

        employee_id_input = (self.page.get_by_text("Employee Id")
                             .locator("..")
                            .locator("..")
                            .locator(".oxd-input"))
        init_id = employee_id_input.input_value()
        final_id = init_id + "_42"
        employee_id_input.fill(final_id)

        self.page.get_by_role("button", name="Save").click()
        expect(self.page.get_by_text("Successfully saved")).to_be_visible()
