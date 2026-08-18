from playwright.sync_api import Page
from pages.example_domain_page import ExampleDomainPage

def test_titolo_pagina_pom(page: Page):
    example_page = ExampleDomainPage(page)
    example_page.navigate()
    assert example_page.get_main_title_text() == "Example Domain"

def test_link_info_pom(page: Page):
    example_page = ExampleDomainPage(page)
    example_page.navigate()
    assert "More information..." in example_page.get_info_link_text()