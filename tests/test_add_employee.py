import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.wait_for_url("**/dashboard/index", timeout=30000)
    expect(page.get_by_role("heading")).to_contain_text("Dashboard")
    page.get_by_role("link", name="PIM").click()
    page.get_by_role("button", name=" Add").click()
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").fill("ahmad")
    page.get_by_role("textbox", name="Middle Name").click()
    page.get_by_role("textbox", name="Middle Name").fill("nahi")
    page.get_by_role("textbox", name="Last Name").click()
    page.get_by_role("textbox", name="Last Name").fill("hanani")
    page.get_by_role("button", name="Save").click()
    expect(page.locator("#oxd-toaster_1")).to_contain_text("Success")
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/210")
    expect(page.locator("#app")).to_contain_text("Personal Details")

