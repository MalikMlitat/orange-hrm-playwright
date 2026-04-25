import pytest
from playwright.sync_api import Page

from data.Candidate import Candidate
from data.Employee import Employee
from data.Vacancy import Vacancy


@pytest.fixture
def add_employee(page: Page, login_with_admin, request):
    """Creates an employee via API and deletes it after the test.
    Accepts an optional Employee via indirect parametrize; falls back to a random one.
    """
    employee: Employee = getattr(request, "param", None) or Employee()
    response = page.request.post(
        url="/web/index.php/api/v2/pim/employees",
        data={
            "firstName": employee.first,
            "middleName": employee.middle,
            "lastName": employee.last,
            "empPicture": None,
            "employeeId": "",
        },
    )
    assert response.ok, f"Failed to create employee via API: {response.text()}"
    employee.emp_number = response.json()["data"]["empNumber"]
    assert employee.emp_number is not None, (
        f"Failed to create employee via API: {employee.emp_number}"
    )
    yield employee
    delete_response = page.request.delete(
        url="/web/index.php/api/v2/pim/employees",
        data={"ids": [employee.emp_number]},
        headers={"Content-Type": "application/json"},
    )
    assert delete_response.ok, (
        f"Failed to delete employee via API: {delete_response.text()}"
    )


@pytest.fixture
def add_vacancy(page: Page, login_with_admin, add_employee, request):
    """Creates a vacancy via API and deletes it after the test.
    Depends on add_employee for the hiring manager.
    Accepts an optional Vacancy via indirect parametrize; falls back to a random one.
    """
    vacancy: Vacancy = getattr(request, "param", None) or Vacancy()

    job_titles_response = page.request.get(url="/web/index.php/api/v2/admin/job-titles")
    assert job_titles_response.ok, (
        f"Failed to fetch job titles: {job_titles_response.text()}"
    )
    job_titles = job_titles_response.json()["data"]
    assert len(job_titles) > 0, "No job titles found — cannot create vacancy"
    vacancy.job_title_id = job_titles[0]["id"]
    vacancy.employee_id = add_employee.emp_number

    response = page.request.post(
        url="/web/index.php/api/v2/recruitment/vacancies",
        data={
            "name": vacancy.name,
            "jobTitleId": vacancy.job_title_id,
            "employeeId": vacancy.employee_id,
            "numOfPositions": vacancy.num_of_positions,
            "description": vacancy.description,
            "status": vacancy.status,
            "isPublished": vacancy.is_published,
        },
    )
    assert response.ok, f"Failed to create vacancy via API: {response.text()}"
    vacancy.id = response.json()["data"]["id"]
    assert vacancy.id is not None, "Failed to retrieve vacancy id from API response"

    yield vacancy

    delete_response = page.request.delete(
        url="/web/index.php/api/v2/recruitment/vacancies",
        data={"ids": [vacancy.id]},
        headers={"Content-Type": "application/json"},
    )
    assert delete_response.ok, (
        f"Failed to delete vacancy via API: {delete_response.text()}"
    )


@pytest.fixture
def add_candidate(page: Page, login_with_admin, add_vacancy, request):
    """Creates a candidate via API and deletes it after the test.
    Depends on add_vacancy for the vacancy link.
    Accepts an optional Candidate via indirect parametrize; falls back to a random one.
    """
    candidate: Candidate = getattr(request, "param", None) or Candidate()
    candidate.vacancy_id = add_vacancy.id

    response = page.request.post(
        url="/web/index.php/api/v2/recruitment/candidates",
        data={
            "firstName": candidate.first,
            "middleName": candidate.middle,
            "lastName": candidate.last,
            "email": candidate.email,
            "vacancyId": candidate.vacancy_id,
            "consentToKeepData": candidate.consent_to_keep_data,
        },
    )
    assert response.ok, f"Failed to create candidate via API: {response.text()}"
    candidate.id = response.json()["data"]["id"]
    assert candidate.id is not None, "Failed to retrieve candidate id from API response"

    yield candidate

    delete_response = page.request.delete(
        url="/web/index.php/api/v2/recruitment/candidates",
        data={"ids": [candidate.id]},
        headers={"Content-Type": "application/json"},
    )
    assert delete_response.ok, (
        f"Failed to delete candidate via API: {delete_response.text()}"
    )
