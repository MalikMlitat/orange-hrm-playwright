import pytest

from pages.login_page import LoginPage
from pages.vacancy_page import VacancyPage


@pytest.fixture()
def login_admin(page):
    login = LoginPage(page)
    # login.navigate()
    login.login("Admin", "admin123")

    page.get_by_role("heading", name="Dashboard").wait_for(state="visible")

    return page


@pytest.fixture()
def vacancy_page(login_admin):
    vacancy = VacancyPage(login_admin)
    return vacancy


@pytest.mark.parametrize(
    ("vacancy_name", "job_title", "manager", "active"),
    [
        ("Job 1", "Account Assistant", "priya  crew", True),
        ("Job 2", "Content Specialist", "priya  crew", False),
        ("Job 3", "Financial Analyst", "priya  crew", True),
    ],
)
def test_add_vacancy(vacancy_page, vacancy_name, job_title, manager, active):
    vacancy_page.navigate_to_vacancies()
    vacancy_page.add_vacancy(vacancy_name, job_title, manager, active)

    vacancy_page.page.locator("text=Add Vacancy").wait_for(state="visible")
