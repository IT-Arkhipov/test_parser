from selene import browser
import pytest
from init import settings
import allure
from allure_commons.types import AttachmentType


def pytest_addoption(parser):
    parser.addoption('--password', default='not set')


@pytest.fixture
def init_config(request):

    settings.password = request.config.getoption('--password')

    yield

    allure.attach(settings.password, 'password', AttachmentType.TEXT, '.txt')
    browser.quit()
