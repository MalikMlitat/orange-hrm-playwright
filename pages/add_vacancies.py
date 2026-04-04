import time
from playwright.sync_api import  expect
class RecruitmentPage:

    def __init__(self, page):
        self.page = page

    def go_to_recruitment_page(self):
        self.page.get_by_role("link", name="Recruitment").click()

    def open_vacancies(self):
        self.page.get_by_role("link", name="Vacancies").click()

    def click_add(self):
        self.page.get_by_role("button", name="Add").click()

    def fill_vacancy_form(self, vacancy_name, description, job_title ,position_no,  manager , is_active):
        self.page.get_by_role("textbox").nth(1).fill(vacancy_name)
        self.page.get_by_text("-- Select --").click()
        self.page.get_by_text(job_title).click()
        self.page.get_by_role("textbox", name="Type description here").fill(description)
        self.page.get_by_role("textbox", name="Type for hints...").fill(manager)
        self.page.get_by_text(manager).click()
        self.page.get_by_role("textbox").nth(4).fill(position_no)
        if is_active :
         self.page.locator(".oxd-switch-input").first.click()


    def save(self):
        self.page.get_by_role("button", name="Save").click()

    def assert_success(self):
        expect(self.page.get_by_text("Edit Vacancy")).to_be_visible(timeout=10000)
        
      


    def delete_vacancy(self, vacancy_name):
     vacancy_name = vacancy_name.strip()
     print("Trying to delete:", vacancy_name)
     row = self.page.locator("div[role='row']", has_text=vacancy_name)
     row.locator("button:has(i.bi-trash)").click()    
     self.page.get_by_role("button", name=" Yes, Delete ").click()
     
       
     
    
    def success_delete (self):
        expect(self.page.get_by_text("Successfully Deleted")).to_be_visible()