import allure
from allure_commons.types import Severity

from init import settings


def test_parser(init_config):
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Repo issues")
    allure.dynamic.story("The #76 issue presence")
    allure.dynamic.link("https://github.com", name="GitHub website")

    with allure.step('GitHub main page open'):
        assert settings.password == '556677'
