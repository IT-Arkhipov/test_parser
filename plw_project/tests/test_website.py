import re
import time

import pytest
from playwright.sync_api import Page, expect
from plw_project.pages.import_pages import *


class TestHerokuapp:

    # @pytest.fixture(autouse=True)
    # @pytest.fixture
    # def page(self, page: Page) -> HerokuappPage:
    #     page = HerokuappPage(page)
    #     page.open()
    #     return page

    # class setup using conftest.setup_class fixture
    page = None

    @pytest.mark.parametrize('text', ('Welcome to the-internet', 'Available Examples'))
    def test_check_heading_text(self, text) -> None:
        assert self.page.is_heading_visible(text), f"Heading '{text}' not visible"


@pytest.mark.usefixture('setup_class')
class TestAddRemove:

    # @pytest.fixture
    # def page(self, page: Page) -> AddRemovePage:
    #     page = AddRemovePage(page)
    #     page.open()
    #     return page

    # class setup using conftest.setup_class fixture
    page = None

    @pytest.mark.parametrize('text', ['Add/Remove Elements'])
    def test_check_heading_text(self, text):
        assert self.page.is_heading_visible(text), f"Heading '{text}' not visible"
        self.page.page.screenshot(type='png', path='test_add_remove.png')

    def test_add_delete_one_click(self, page: AddRemovePage):
        time.sleep(1)
        page.click_button('Add Element')
        assert page.is_button_visible('Delete'), f"Button 'Delete' not visible"
        time.sleep(1)

        page.click_button('Delete')
        assert not page.is_button_visible('Delete'), f"Button 'Delete' still visible"
        time.sleep(1)
