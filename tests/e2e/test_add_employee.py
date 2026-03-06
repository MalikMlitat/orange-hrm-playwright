from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.add_employee_page import AddEmployeePage


def test_add_employee(page: Page):

    login = LoginPage(page)
    dashboard = DashboardPage(page)
    employee = AddEmployeePage(page)

    login.navigate()
    login.login("Admin", "admin123")

    dashboard.go_to_pim()

    employee.add_employee("hala", "abed", "shream")