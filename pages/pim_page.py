from playwright.sync_api import Page


class PimPage:
    def __init__(self, page: Page):
        self.page = page
        self.pim_menu = 'a:has-text("PIM")'
        self.employee_name_input = 'input[placeholder="Type for hints..."]'
        self.employee_id_input = '(//input[@class="oxd-input oxd-input--active"])[2]'
        self.table_rows = ".oxd-table-body .oxd-table-row"

    def go_to_pim(self):
        """Navigate to PIM page."""
        self.page.click(self.pim_menu)
        self.page.wait_for_url("**/web/index.php/pim/viewEmployeeList", timeout=5000)
        self.page.locator(self.employee_id_input).wait_for(timeout=5000)

    def search_by_id(self, emp_id):
        """Search employee by ID."""
        self.page.locator('(//input[contains(@class,"oxd-input")])[2]').fill(emp_id)
        self.page.click("button:has-text('Search')")
        self.page.wait_for_selector(".oxd-loading-spinner", state="hidden")

    def search_by_name(self, name):
        """Search employee by name."""
        self.page.fill('input[placeholder="Type for hints..."]', name)
        # self.page.wait_for_selector(".oxd-autocomplete-dropdown")
        # self.page.click(f"text={name}")
        self.page.click("button:has-text('Search')")
        # self.page.wait_for_selector(".oxd-table-body .oxd-table-row")

    def get_search_results(self):
        """Get search results."""
        rows = self.page.locator(".oxd-table-body .oxd-table-row")

        results = []

        count = rows.count()

        for i in range(count):
            row = rows.nth(i)

            cells = row.locator(".oxd-table-cell")

            emp_id = cells.nth(1).inner_text().strip()
            emp_name = cells.nth(2).inner_text().strip()

            results.append((emp_id, emp_name))

        return results
