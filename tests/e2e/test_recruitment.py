import pytest
from playwright.sync_api import Page, expect

from data.Candidate import Candidate
from data.Vacancy import Vacancy


@pytest.mark.parametrize(
    "add_vacancy", [Vacancy(name="Senior QA Engineer")], indirect=True
)
def test_vacancy_created_via_api_is_visible_in_list(page: Page, add_vacancy):
    page.goto("/web/index.php/recruitment/viewJobVacancy")
    expect(page.get_by_text(add_vacancy.name)).to_be_visible()


@pytest.mark.parametrize(
    "add_candidate",
    [Candidate(first="Jane", last="Recruiter")],
    indirect=True,
)
def test_candidate_created_via_api_is_visible_in_list(page: Page, add_candidate):
    page.goto("/web/index.php/recruitment/viewCandidates")
    expect(
        page.get_by_text(
            f"{add_candidate.first} {add_candidate.middle} {add_candidate.last}"
        )
    ).to_be_visible()
