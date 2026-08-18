import base64
import pytest
import pytest_html

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            # 1. Cattura lo screenshot in memoria come byte
            screenshot_bytes = page.screenshot()
            
            # 2. Converti i byte in una stringa Base64
            screenshot_b64 = base64.b64encode(screenshot_bytes).decode("utf-8")
            
            # 3. Incorpora l'immagine direttamente nell'HTML
            html_img = f'<div><p><b>Screenshot Errore:</b></p><img src="data:image/png;base64,{screenshot_b64}" style="width:600px; max-width:100%; border:1px solid red;"/></div>'
            
            extra.append(pytest_html.extras.html(html_img))
            report.extra = extra