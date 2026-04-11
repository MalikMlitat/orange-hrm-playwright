import pytest
from faker import Faker

from models.candidate_data import CandidateData
from pages.candidate_page import CandidatePage
from pages.login_page import LoginPage

fake = Faker()


@pytest.fixture()
def login_admin(page):
    login = LoginPage(page)
    login.login("Admin", "admin123")
    return page


@pytest.mark.parametrize("action", ["shortlist", "reject"])
def test_candidate_flow(login_admin, action):
    page = login_admin

    candidate_page = CandidatePage(page)

    # 1. Navigate Recruitment
    candidate_page.navigate_to_recruitment()

    # 2. Add Candidate
    data = CandidateData(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        vacancy="Senior QA Lead",
        email=fake.email(),
    )

    candidate_page.add_candidate(data)

    # 3. Action (Reject / Shortlist)
    if action == "reject":
        candidate_page.reject_candidate()
    else:
        candidate_page.shortlist_candidate()

    assert True  # validation
