import pytest
import random
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage
from utils.pw_tracing import pw_tracing


# بيانات الاختبار
VACANCIES_DATA = [
    ("QA Engineer", "Saher_Task", "Linda"),
]


@pytest.fixture
def recruitment_setup(page: Page):

    page.set_default_timeout(30000)

    # Login
    login_pg = LoginPage(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_pg.login("Admin", "admin123")

    rec_pg = RecruitmentPage(page)

    created_vacancies = []

    yield rec_pg, created_vacancies

    # Cleanup
    for name in created_vacancies:
        try:
            rec_pg.delete_vacancy(name)
        except:
            pass


@pw_tracing
@pytest.mark.parametrize("job_title, base_name, manager", VACANCIES_DATA)
def test_add_vacancy_process(page: Page, recruitment_setup, job_title, base_name, manager):

    rec_pg, created_list = recruitment_setup

    # إنشاء اسم فريد
    unique_name = f"{base_name}_{random.randint(100,999)}"

    created_list.append(unique_name)

    # إضافة الوظيفة
    rec_pg.add_vacancy(job_title, unique_name, manager)

    # التأكد من ظهورها في الجدول
    rec_pg.navigate_to_vacancies()

    expect(
        page.get_by_role("row").filter(has_text=unique_name)
    ).to_be_visible()