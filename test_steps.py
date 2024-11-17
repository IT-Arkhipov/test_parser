import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class Browser:

    def __init__(self, driver):
        self.driver = driver

    def element(self, selector):
        return Element_(selector, self.driver)


class Element:
    def __init__(self, web_element, driver):
        self.web_element = web_element
        self.driver = driver

    def click_element(self):
        ActionChains(self.driver).click(self.web_element).perform()


class Element_:
    def __init__(self, selector, driver):
        self.selector = selector
        self.driver = driver

    @property
    def web_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.selector)

    def click_element(self):
        ActionChains(self.driver).click(self.web_element).perform()


def test_parser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # driver.implicitly_wait(1.0)
    browser = Browser(driver)
    wait = WebDriverWait(driver, 0.5)

    driver.get('https://demoqa.com/automation-practice-form')

    element = driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]')
    wait.until(EC.element_to_be_clickable(element))
    element.click()

    # wait = WebDriverWait(driver, timeout=2)

    # driver.get('https://ecosia.com')
    # driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]').send_keys('selene' + Keys.ENTER)

    # search_field = driver.find_element(By.CSS_SELECTOR, '[data-test-id="search-form-input"]')
    # search_field.send_keys('selene' + Keys.ENTER)

    # article_link = driver.find_elements(
    #     By.CSS_SELECTOR, '[data-test-id="mainline-result-web"]'
    # )[0].find_element(By.CSS_SELECTOR, '.result__title')

    # selector = '[data-test-id="mainline-result-web"]:nth-of-type(2) .result__title'
    # article_link.click()

    # click_element(driver, article_link)

    # Element(article_link, driver).click_element()


    # def element(selector):
    #     return browser.element(selector)
    #
    # my_element = element(selector)
    #
    # my_element.click_element()

    # Element_(selector, driver).click_element()

    time.sleep(2)
