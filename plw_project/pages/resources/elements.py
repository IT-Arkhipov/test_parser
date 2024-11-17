from dataclasses import dataclass


@dataclass
class Roles:
    role: str = ''
    name: str = ''


add_element_btn = Roles(role='button', name='Add Element')
delete_btn = Roles(role='button', name='Delete')


class Locators:
    add_element_btn_css = '.example>button'
    add_element_btn = '//button[text()="Add Element"]'
    delete_btn = '//button[text()="Delete"]'


locator_ = Locators()


class AddRemovePageLocators:
    add_element_btn_css = '.example>button'
    add_element_btn = '//button[text()="Add Element"]'
    delete_btn = '//button[text()="Delete"]'


add_remove_page_locators = AddRemovePageLocators()
