import functools
import time
from pathlib import Path
from typing import Any
from playwright.sync_api import Page

def pw_tracing(func):
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # البحث عن كائن الصفحة في المعاملات
        page = kwargs.get("page") or (
            args[0] if args and isinstance(args[0], Page) else None
        )
        if page is None:
            # محاولة البحث في الأعضاء (للـ Page Objects)
            page = getattr(args[0], 'page', None) if args else None

        if page:
            test_name = func.__name__
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            trace_dir = Path("test_traces") / f"{test_name}_{timestamp}"
            trace_dir.mkdir(parents=True, exist_ok=True)

            # بدء التتبع ومجموعات الخطوات
            page.context.tracing.start(screenshots=True, snapshots=True)
            page.context.tracing.group(f"Executing: {test_name}")
            
            try:
                result = func(*args, **kwargs)
                page.context.tracing.group_end()
                page.context.tracing.stop(path=str(trace_dir / "trace.zip"))
                return result
            except Exception as e:
                page.context.tracing.group_end()
                page.screenshot(path=str(trace_dir / "error_screenshot.png"))
                page.context.tracing.stop(path=str(trace_dir / "trace.zip"))
                raise e
        return func(*args, **kwargs)
    return wrapper