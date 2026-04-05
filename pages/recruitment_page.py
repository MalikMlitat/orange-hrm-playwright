from playwright.sync_api import Page, expect


class RecruitmentPage:

    def __init__(self, page: Page):
        self.page = page

        # Navigation
        self.recruitment_menu = page.get_by_role("link", name="Recruitment", exact=True)
        self.vacancies_menu = page.get_by_role("link", name="Vacancies")

        # Buttons
        self.add_btn = page.get_by_role("button", name="Add")
        self.save_btn = page.get_by_role("button", name="Save")

        # Form fields
        self.job_title_dropdown = page.locator(".oxd-select-text").first
        self.vacancy_name_input = page.locator(".oxd-input--active").nth(1)

        self.hiring_manager_input = page.get_by_placeholder("Type for hints...")

        self.active_toggle = page.locator(".oxd-switch-input")

        # Success message
        self.toast = page.locator(".oxd-toast-content")

    # Navigation

    def navigate_to_vacancies(self):

        self.recruitment_menu.click()
        self.vacancies_menu.click()

    # Add Vacancy

    def add_vacancy(self, job_title, vacancy_name, manager_query, is_active=True):

        self.navigate_to_vacancies()

        self.add_btn.click()

        # Job Title
        self.job_title_dropdown.click()
        self.page.get_by_role("option", name=job_title).click()

        # Vacancy Name
        self.vacancy_name_input.fill(vacancy_name)

        # Hiring Manager
        self.select_hiring_manager(manager_query)

        # Active toggle
        if not is_active:
            self.active_toggle.click()

        # Save
        self.save_btn.click()

        # Validation
        expect(self.toast).to_be_visible(timeout=10000)

    # Hiring Manager Selection

    def select_hiring_manager(self, manager_name):

    # كتابة اسم المدير
        self.hiring_manager_input.fill(manager_name)

    # انتظار ظهور القائمة
    dropdown = self.page.locator(".oxd-autocomplete-dropdown")

    dropdown.wait_for(state="visible")

    # اختيار المدير بالاسم
    self.page.locator(".oxd-autocomplete-dropdown div", has_text=manager_name).first.click()

    # Delete Vacancy

    def delete_vacancy(self, vacancy_name):

        self.navigate_to_vacancies()

        row = self.page.get_by_role("row").filter(has_text=vacancy_name)

        if row.count() > 0:

            row.locator("i.bi-trash").click()

            self.page.get_by_role("button", name="Yes, Delete").click()

            expect(self.toast).to_be_visible()