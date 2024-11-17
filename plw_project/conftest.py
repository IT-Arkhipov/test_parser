import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from plw_project.pages.add_remove import AddRemovePage


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


# @pytest.fixture(scope="class")
# def setup_class(request, page: Page):
#     def convert_class_name(class_name: str):
#         result = ""
#         for char in class_name.replace("Test", ""):
#             if char.isupper():
#                 result += "_" + char.lower()
#             else:
#                 result += char
#         return result.lstrip("_")
#
#     class_name = request.cls.__name__
#     page_class = AddRemovePage
#
#     # Create the page object
#     page_obj = page_class(page)
#
#     # Inject the object into the test class
#     setattr(request.cls, 'page', page)
#     setattr(request.cls, f'{convert_class_name(class_name)}', page_obj)
#
#     print(f"Setting up {class_name}")
#     page_obj.open()
#     yield
