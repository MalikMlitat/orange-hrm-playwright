import pytest
from playwright.sync_api import Page, expect

from data.Employee import Employee
from pages import pim
from pages.pim_page import PimPage


def test_add_employee_without_creds(page: Page, login_with_admin):
    pim = PimPage(page)
    add_employee_page = pim.visit_tab_add_employee()
    add_employee_page.add_employee_without_details()


@pytest.mark.parametrize("employee", [
    Employee(),
    Employee(pic_path="data/profile_pic.jpeg"),
])
def test_add_employee_with_differt_first_names(page: Page, login_with_admin, employee):
    pim = PimPage(page)
    add_employee_page = pim.visit_tab_add_employee()
    add_employee_page.add_employee_without_details(employee=employee)


@pytest.mark.parametrize("add_employee", [Employee(first="Malik"),
                                          Employee(last="Alipapa"),
                                          Employee()
                                          ], indirect=True)
def test_api_employee_personal_details_visible(page: Page, add_employee):
    page.goto(f"/web/index.php/pim/viewPersonalDetails/empNumber/{add_employee.emp_number}")
    expect(page.get_by_role("heading", name="Personal Details")).to_be_visible()















@pytest.mark.parametrize("add_employee",
                         [Employee(first="Malik")])
def test_employee_created_via_api_is_visible_in_list(page: Page, add_employee):
    page.goto(f"/web/index.php/pim/viewPersonalDetails/empNumber/{add_employee.emp_number}")
    expect(page.get_by_role("heading", name="Personal Details")).to_be_visible()
    expect(page.get_by_text(f"{add_employee.first} {add_employee.last}")).to_be_visible()
