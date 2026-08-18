from playwright.sync_api import Page

class ExampleDomainPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://example.com"
        self.main_title = page.locator("h1")
        self.info_link = page.locator("text=More information...")

    def navigate(self):
        self.page.goto(self.url)

    def get_main_title_text(self):
        return self.main_title.inner_text()

    def get_info_link_text(self):
        return self.info_link.inner_text()