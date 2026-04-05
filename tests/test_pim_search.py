import pytest
from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from utils.pw_tracing import pw_tracing

@pytest.fixture
def pim_setup(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_pg = LoginPage(page)
    login_pg.login("Admin", "admin123")
    return PIMPage(page)

@pw_tracing
def test_complete_pim_lifecycle(page, pim_setup):
    pim_pg = pim_setup
    first, last = "Saher", "Tester"
    
    # 1. إضافة موظف
    pim_pg.add_employee(first, last)
    
    # الحصول على الـ ID تلقائياً (اختياري) أو استخدامه إذا كان ثابتاً
    # لنفترض أننا سنبحث بالاسم الذي أضفناه
    
    # 2. البحث (Positive Case)
    pim_pg.search_employee("") # يمكن تعديلها للبحث بالاسم
    
    # 3. التنظيف (Cleanup) - حذف الموظف
    # ملاحظة: يفضل عمل الحذف في fixture teardown لضمان التنفيذ
    print("Cleanup: Employee should be deleted here")