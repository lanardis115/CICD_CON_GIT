from playwright.sync_api import Page, expect

def test_titolo_pagina(page: Page):
    page.goto("https://example.com")
    expect(page).to_have_title("Example Domain")

def test_testo_intestazione(page: Page):
    page.goto("https://example.com")
    header = page.locator("h1")
    expect(header).to_have_text("Example Domain")