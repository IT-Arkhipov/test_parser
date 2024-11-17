from playwright.sync_api import Page, expect


def test_wikipedia(page: Page):
    page.goto("https://www.wikipedia.org/")
    page.get_by_role('link', name='Русский').click()
    expect(page.get_by_text("Добро пожаловать в Википедию")).to_be_visible()


def test_wikipedia_2(page: Page):
    page.goto("https://www.wikipedia.org/")
    page.get_by_role('link', name='Русский').click()
    page.get_by_role('link', name='Содержание').click()
    page.locator('#ca-talk').click()
    expect(page.locator('#firstHeading')).to_have_text("Обсуждение Википедии:Содержание")
