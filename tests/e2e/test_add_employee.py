
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.pim_page import PimPage
from pages.pim.add_employee_page import AddEMployeePage


def test_add_employee_without_creads(page: Page, login_with_admin):

    # LoginPage(page).login_with_valid_admin()
    pim = PimPage(page)
    add_employee_page = pim.visible_tab_add_employee()
    add_employee_page.add_employee_without_details(first="Wafaa",
                                        middle="Khaled",
                                        last="Alastal"
                                        )