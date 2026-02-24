import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "toz contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


def login(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()


def employeeDetails(page, firstName, lastName, Id):
    page.get_by_role("link", name="PIM").click()
    page.get_by_role("link", name="Add Employee").click()

    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").fill(firstName)
    page.get_by_role("textbox", name="Last Name").click()
    page.get_by_role("textbox", name="Last Name").fill(lastName)
    page.get_by_role("textbox").nth(4).click()
    page.get_by_role("textbox").nth(4).fill(Id)


def testAddEmployeeMismatchedPasswords(page: Page) -> None:
    login(page)
    page.get_by_role("link", name="PIM").click()
    page.get_by_role("link", name="Add Employee").click()

    # page.get_by_role("textbox", name="First Name").click()
    # page.get_by_role("textbox", name="First Name").fill("layal")
    # page.get_by_role("textbox").nth(4).click()
    # page.get_by_role("textbox").nth(4).fill("1111")
    # page.get_by_role("textbox", name="Last Name").click()
    # page.get_by_role("textbox", name="Last Name").fill("f")

    employeeDetails(page, "layal", "f", "1111")
    page.locator(".oxd-switch-input").click()
    page.get_by_role("textbox").nth(5).click()
    page.get_by_role("textbox").nth(5).fill("layal")
    page.locator('input[type="password"]').nth(1).click()
    page.locator('input[type="password"]').first.click()
    page.locator('input[type="password"]').first.fill("123456layal")
    page.locator('input[type="password"]').nth(1).click()
    page.locator('input[type="password"]').nth(1).fill("123456")
    page.get_by_role("button", name="Save").click()
    expect(page.get_by_text("Passwords do not match")).to_be_visible()


def testAddEmployeeSuccess(page: Page) -> None:
    login(page)
    employeeDetails(page, "layal", "f", "1111")
    page.locator(".oxd-switch-input").click()
    page.locator('input[type="password"]').first.click()
    page.locator('input[type="password"]').nth(1).click()
    page.locator('input[type="password"]').nth(1).fill("123456layal")
    page.get_by_role("button", name="Save").click()
    page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/186"
    )


def testAddEmployeeWithExistId(page: Page) -> None:
    login(page)
    employeeDetails(page, "layal", "f", "1111")
    page.get_by_role("button", name="Save").click()
    expect(page.get_by_text("Employee ID already exists")).to_be_visible()


def testAddEmployeeWithInvalidAttachmentSize(page: Page) -> None:
    login(page)
    employeeDetails(page, "layal", "f", "888")
    page.get_by_role("button", name="Choose File").set_input_files("../../attachments/b.jpg")
    page.locator("form").get_by_role("img", name="profile picture").click()
    page.get_by_role("button", name="Save").click()
    # fail
    # expect(page.get_by_text("Invalid file size")).to_be_visible()
    expect(page.get_by_text("Attachment Size Exceeded")).to_be_visible()


def testAddEmployeeWithValidAttachmentSize(page: Page) -> None:
    login(page)
    employeeDetails(page, "layal", "f", "888")
    page.get_by_role("button", name="Choose File").set_input_files([])
    page.get_by_role("button").nth(4).click()
    page.get_by_role("button", name="Choose File").set_input_files(
        "../../attachments/image.png"
    )
    page.get_by_role("button", name="Save").click()
    page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/173"
    )
