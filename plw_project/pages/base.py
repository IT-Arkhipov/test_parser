from typing import Callable

from playwright.sync_api import Page, Locator
from dataclasses import dataclass


element = {
    'button': lambda self, name: self.page.get_by_role('button', name=name)
}


@dataclass
class Elements:
    element: Callable


button_ = Elements(element=lambda self, name: self.page.get_by_role('button', name=name))


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = ''

    def open(self):
        self.page.goto(self.url)

    def locate_(self, selector) -> Locator:
        return self.page.locator(selector)

    def get_by_role(self, role, name) -> Locator:
        return self.page.get_by_role(role, name=name)

    def click_button(self, name):
        self.button(name).click()

    def button(self, name) -> Locator:
        got_button = button_.element(self, name)
        return got_button

    def get_element(self, locator_):
        return self.page.locator(locator_)

    def click_button_locator(self, locator_):
        self.get_element(locator_).click()

    def is_button_visible(self, name) -> bool:
        return self.button('Delete').is_visible()

    def is_heading_visible(self, text) -> bool:
        return self.page.get_by_role('heading', name=text, exact=True).is_visible()

    def get_element_text(self, selector):
        return self.page.locator(selector).inner_text()
