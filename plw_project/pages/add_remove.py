from plw_project.pages.base import BasePage
from playwright.sync_api import Page


class AddRemovePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = 'https://the-internet.herokuapp.com/add_remove_elements/'
