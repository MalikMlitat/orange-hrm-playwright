from pages.login_page import LoginPage
from pages.pim_page import PIMPage


def test_add_employee(page):

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", timeout=60000)
    login_pg = LoginPage(page)
    pim_pg = PIMPage(page)

    login_pg.login("Admin", "admin123")

    pim_pg.add_employee("Saher", "Hijazi")