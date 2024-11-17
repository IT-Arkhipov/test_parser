import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from plw_project.pages.import_pages import *


# def pytest_addoption(parser):
#     """Add the custom command-line option `--headed` to pytest.
#     """
#     parser.addoption(
#         "--headed",
#         action="store_true",
#         default=False,
#         help="Run tests in headed mode"
#     )


@pytest.fixture(scope='class')
def is_headless(request):
    """    Fixture to check if the --headed option is present.
    Returns True if --headed is specified, otherwise False.
    """
    return not request.config.getoption("--headed")


@pytest.fixture(scope='class')
def page(is_headless) -> Page:
    with sync_playwright() as p:
        browser = p.chromium.launch(args=['--start-maximized'], headless=False)
        page = browser.new_page(no_viewport=True)

        yield page

        page.close()
        browser.close()


class_name = {
    'TestAddRemove': AddRemovePage,
    'TestHerokuapp': HerokuappPage
}


@pytest.fixture(scope="class", autouse=True)
def setup_class(request, page: Page):
    # Create the page object
    page_class = class_name.get(request.cls.__name__)
    page_obj = page_class(page)

    # Inject the object into the test class
    setattr(request.cls, 'page', page_obj)
    page_obj.open()

    yield


