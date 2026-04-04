
from playwright.sync_api import Page
import pytest

from pages.add_vacancies import RecruitmentPage

@pytest.mark.parametrize(
    "vacancy_name, job_title, description, hiring_manager, position_no , is_active",
    [  
        ("software enasd", "QA Lead" , "test by enas, tester, qa, python", "Thomas Kutty Benny", "2" , True),     
        ("tester2 enas ss", "Account Assistant","test by enas, tester, qa", "Thomas Kutty Benny", "6",False),
        ("quality2 enassss ", "Database Administrator", "test", "Thomas Kutty Benny", "9",True)
    ]
)
def test_add_vacancies(logged_in_page: Page,job_title, cleanup_vacancies,    vacancy_name, description, hiring_manager, position_no , is_active):

    add_vacancy = RecruitmentPage(logged_in_page)

    add_vacancy.go_to_recruitment_page()
    add_vacancy.open_vacancies()
    add_vacancy.click_add()
    add_vacancy.fill_vacancy_form(
        vacancy_name=vacancy_name,
        description=description,
        job_title=job_title,
        manager=hiring_manager,
        position_no=position_no,
        is_active=is_active
    )
    add_vacancy.save()
    add_vacancy.assert_success()
    cleanup_vacancies.append(vacancy_name.strip())
    
    
   
   
