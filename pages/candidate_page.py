from playwright.sync_api import Page


class CandidatePage:
    def __init__(self, page: Page):
        self.page = page

    # -------------------------
    # NAVIGATION
    # -------------------------
    def navigate_to_recruitment(self):
        self.page.get_by_role("link", name="Recruitment").click()
        self.page.get_by_role("link", name="Candidates").click()
        self.page.locator("h5:has-text('Candidates')").wait_for(state="visible")

    # -------------------------
    # ADD CANDIDATE
    # -------------------------
    def click_add(self):
        self.page.get_by_role("button", name="Add").click()

    def add_candidate(self, data):
        self.click_add()

        self.page.get_by_placeholder("First Name").fill(data.first_name)
        self.page.get_by_placeholder("Last Name").fill(data.last_name)

        self.page.get_by_text("-- Select --").click()
        self.page.get_by_role("option", name=data.vacancy).click()

        self.page.get_by_placeholder("Type here").nth(0).fill(data.email)

        self.page.get_by_role("button", name="Save").click()

    # -------------------------
    # ACTIONS (REJECT / SHORTLIST)
    # -------------------------
    def shortlist_candidate(self):
        self.page.get_by_role("button", name="Shortlist").click()
        self.page.locator("h6:has-text('Shortlist Candidate')").wait_for(state="visible")
        self.page.get_by_placeholder("Type here").fill("sample note for shortlisted candidate")
        self.page.get_by_role("button", name="Save").click()

    def reject_candidate(self):
        self.page.get_by_role("button", name="Reject").click()
        self.page.locator("h6:has-text('Reject Candidate')").wait_for(state="visible")
        self.page.get_by_placeholder("Type here").fill("sample note for rejected candidate")
        self.page.get_by_role("button", name="Save").click()
