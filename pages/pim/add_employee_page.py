from playwright.sync_api import Page, expect

class AddEMployeePage:
    def __init__(self, page: Page):
        self.page = page

    def add_employee_without_details(self, first, middle, last):
        self.page.get_by_placeholder("First Name").fill(first)
        self.page.get_by_placeholder("Middle Name").fill(middle)
        self.page.get_by_placeholder("Last Name").fill(last)

        # employee_id_input = (self.page.get_by_label("Employee Id")
        # .locator("..")
        # .locator("..")
        # .locator(".oxd-input").fill(last)
        # )

        employee_id_input = self.page.locator("input.oxd-input").nth(4)


        init_id = employee_id_input.input_value()
        final_id = init_id + "-42"
        employee_id_input.fill(final_id)

        self.page.get_by_role("button", name="Save").click()
        expect(self.page.get_by_text("Successfully saved")).to_be_visible()

