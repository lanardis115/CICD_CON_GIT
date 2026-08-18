import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Intercetta gli errori e allega uno screenshot direttamente dentro il report HTML."""
    outcome = yield
    report = outcome.get_result()
        
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_bytes = page.screenshot(full_page=True)
            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html:
                extra = getattr(report, "extra", [])
                html_img = f'<div><p><b>Screenshot Errore:</b></p><img src="data:image/png;base64,{screenshot_bytes.hex()}" style="width:600px; border:1px solid red;"/></div>'
                extra.append(pytest_html.extras.html(html_img))
                report.extra = extra