import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from data.Employee import Employee


@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getini("base_url")


@pytest.fixture(scope="function", autouse=True)
def goto(page: Page):
    """Fixture to navigate to the base URL."""
    page.goto("/")


@pytest.fixture
def login_with_admin(page: Page):
    LoginPage(page).login_with_valid_admin()


@pytest.fixture
def add_employee(page: Page, login_with_admin, request):
    """Creates an employee via API and deletes it after the test.
    Accepts an optional Employee via indirect parametrize; falls back to a random one.
    """
    # before all
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
    # after_all
    delete_response = page.request.delete(
        url="/web/index.php/api/v2/pim/employees",
        data={"ids": [employee.emp_number]},
        headers={"Content-Type": "application/json"},
    )
    assert delete_response.ok, (
        f"Failed to delete employee via API: {delete_response.text()}"
    )
