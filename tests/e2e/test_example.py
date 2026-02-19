import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def test_login_to_orangehrm(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")

    page.get_by_role("button", name="Login").click()
    expect(page).to_have_title(re.compile("OrangeHRM"))

def test_add_employee(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",timeout=30000)
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index",timeout=60000)
    page.get_by_role("link", name="PIM").click()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList",timeout=60000)
    page.get_by_role("button", name=" Add").click()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee",timeout=60000)
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").fill("mohammed")
    page.get_by_role("textbox", name="Middle Name").click()
    page.get_by_role("textbox", name="Middle Name").fill("ahmed")
    page.get_by_role("textbox", name="Last Name").click()
    page.get_by_role("textbox", name="Last Name").fill("mohammed")
    page.get_by_role("button", name="Save").click()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/181")
    # page.get_by_role("heading", name="Personal Details").click() 
    expect(page.locator("#app")).to_contain_text("Personal Details")