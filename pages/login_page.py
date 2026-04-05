from playwright.sync_api import expect

class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username = page.get_by_role("textbox", name="Username")
        self.password = page.get_by_role("textbox", name="Password")
        self.login_btn = page.get_by_role("button", name="Login")

    def login(self, user, pwd):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()
        
        # التعديل هنا: حددنا أنه "عنوان" (heading) لنتجنب التكرار
        expect(self.page.get_by_role("heading", name="Dashboard")).to_be_visible()