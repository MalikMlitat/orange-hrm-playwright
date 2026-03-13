import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.pim_page import PimPage


@pytest.mark.parametrize(
    ("emp_id", "emp_name"),
    [
        ("0001", None),
        (None, "Orange Test"),
    ],
)
def test_employee_search(page: Page, emp_id, emp_name):
    login = LoginPage(page)
    pim = PimPage(page)

    login.navigate()
    login.login("Admin", "admin123")

    page.wait_for_load_state("networkidle")
    pim.go_to_pim()

    if emp_id:
        pim.search_by_id(emp_id)
        results = pim.get_search_results()
        print(results)
        assert any(emp_id in id for id, _ in results), f"Employee {emp_id} not found."

    if emp_name:
        pim.search_by_name(emp_name)
        results = pim.get_search_results()
        print(results)
        assert any(emp_name.split()[0] in name for _, name in results), f"Employee {emp_name} not found."
