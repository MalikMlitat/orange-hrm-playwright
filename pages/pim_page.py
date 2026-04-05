from playwright.sync_api import expect

class PIMPage:
    def __init__(self, page):
        self.page = page
        self.pim_menu = page.get_by_role("link", name="PIM")
        self.add_emp_link = page.get_by_role("link", name="Add Employee")
        self.first_name = page.get_by_role("textbox", name="First Name")
        self.last_name = page.get_by_role("textbox", name="Last Name")
        self.save_btn = page.get_by_role("button", name="Save")
        
        # محددات البحث
        self.search_id_input = page.get_by_role("textbox").nth(1)
        self.search_btn = page.get_by_role("button", name="Search")
        self.table_row = page.get_by_role("row")

    def add_employee(self, first, last):
        self.pim_menu.click()
        self.add_emp_link.click()
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.save_btn.click()
        expect(self.page.get_by_role("heading", name="Personal Details")).to_be_visible()

    def search_employee(self, emp_id):
        self.pim_menu.click()
        self.search_id_input.fill(emp_id)
        self.search_btn.click()

    def delete_employee(self, emp_id):
        self.search_employee(emp_id)
        # الضغط على زر الحذف في الصف الصحيح
        self.table_row.filter(has_text=emp_id).get_by_role("button").first.click()
        self.page.get_by_role("button", name="Yes, Delete").click()