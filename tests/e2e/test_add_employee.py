from playwright.sync_api import Page


def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="PIM").click()
    page.get_by_role("link", name="Add Employee").click()
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").fill("hala")
    page.get_by_role("textbox", name="Middle Name").click()
    page.get_by_role("textbox", name="Middle Name").fill("abed")
    page.get_by_role("textbox", name="Last Name").click()
    page.get_by_role("textbox", name="Last Name").fill("shream")
    page.get_by_role("button", name="Save").click()
