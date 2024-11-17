import re
import time

import pytest
from playwright.sync_api import Page, expect
from plw_project.pages.import_pages import *


class TestHerokuapp:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page) -> None:
        self.heroku = HerokuappPage(page)
        self.page = self.heroku.page
        self.heroku.open()

    @pytest.mark.parametrize('text', ('Welcome to the-internet', 'Available Examples'))
    def test_check_heading_text(self, text) -> None:
        assert self.heroku.is_heading_visible(text), f"Heading '{text}' not visible"


@pytest.mark.usefixture('setup_class')
class TestAddRemove:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page) -> None:
        self.add_remove = AddRemovePage(page)
        self.page = self.add_remove.page
        self.add_remove.open()

    @pytest.mark.parametrize('text', ['Add/Remove Elements'])
    def test_check_heading_text(self, text):
        assert self.add_remove.is_heading_visible(text), f"Heading '{text}' not visible"

    def test_add_delete_one_click(self):
        time.sleep(1)
        self.add_remove.click_button('Add Element')
        assert self.add_remove.is_button_visible('Delete'), f"Button 'Delete' not visible"
        time.sleep(1)

        self.add_remove.click_button('Delete')
        assert not self.add_remove.is_button_visible('Delete'), f"Button 'Delete' still visible"
        time.sleep(1)
