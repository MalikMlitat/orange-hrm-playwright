from playwright.sync_api import Page

from pages.employee_page import EmployeePage
from pages.login_page import LoginPage


def test_add_employee_without_login(page: Page):
    login = LoginPage(page)
    emp = EmployeePage(page)

    login.navigate()
    login.login("Admin", "admin123")

    emp.open_pim()
    emp.click_add_employee()
    emp.add_employee_without_login("Mohammed", "Adwan")


def test_add_employee_with_login(page: Page):
    login = LoginPage(page)
    emp = EmployeePage(page)

    login.navigate()
    login.login("Admin", "admin123")

    emp.open_pim()
    emp.click_add_employee()
    emp.add_employee_with_login("Ali", "Saleh", "ali_test123", "Password123")
