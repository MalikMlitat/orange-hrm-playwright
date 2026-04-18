import pytest
from playwright.sync_api import sync_playwright

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.vacancies_page import VacanciesPage


@pytest.fixture(scope="session")
def admin_login():
    """Fixture to launch browser, login as Admin once, and provide page for all tests."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)  
        context = browser.new_context()
        page = context.new_page()

    
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("Admin", "admin123")

    
        yield page

        
        context.close()
        browser.close()


@pytest.fixture
def vacancy_factory(admin_login):
    page = admin_login
    dashboard = DashboardPage(page)
    vacancies = VacanciesPage(page)
    created_vacancies = []

    def _create(vacancy_data):
        dashboard.go_to_recruitment()
        vacancies.open_vacancies()
        vacancies.delete_vacancies_by_name(vacancy_data["name"])

        dashboard.go_to_recruitment()
        vacancies.open_vacancies()
        created_vacancies.append(vacancy_data["name"])
        vacancies.add_vacancy(vacancy_data)

        return {
            "page": page,
            "vacancy_name": vacancy_data["name"],
        }

    yield _create

    for vacancy_name in reversed(created_vacancies):
        dashboard.go_to_recruitment()
        vacancies.open_vacancies()
        vacancies.delete_vacancies_by_name(vacancy_name)
