import pytest
from playwright.sync_api import Page


@pytest.fixture(autouse=True)
def _goto(page: Page):
    """Fixture to navigate to the base URL."""
    base_url = "https://opensource-demo.orangehrmlive.com/"
    page._goto(base_url, wait_until="domcontentloaded", timeout=60000)
