import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """إعدادات المتصفح: حجم الشاشة وتجاهل أخطاء الشهادات"""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True,
    }

@pytest.fixture(scope="function", autouse=True)
def goto(page: Page):
    """الانتقال التلقائي للرابط الأساسي قبل كل اختبار"""
    base_url = "https://opensource-demo.orangehrmlive.com/"
    page.goto(base_url)