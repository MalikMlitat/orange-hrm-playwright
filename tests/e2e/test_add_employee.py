import pytest
from playwright.sync_api import Page
from pages.pim_page import PimPage


def test_add_employee_without_creds(page: Page, login_with_admin):

    pim = PimPage(page)

    add_employee_page = pim.visit_tab_add_employee()
    add_employee_page.add_employee_without_details(first="ahmad",
                                         middle="salim",
                                         last="mylastname")


