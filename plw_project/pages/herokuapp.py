from plw_project.pages.base import BasePage
from playwright.sync_api import Page


class HerokuappPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = 'https://the-internet.herokuapp.com/'

    def get_element_text(self, selector):
        return self.page.locator(selector).inner_text()
