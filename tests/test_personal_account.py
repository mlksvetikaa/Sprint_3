from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.data import TestData
from tests.locators import TestLocators


class TestToFromAccount:
    def test_to_account(self, driver):
        driver.find_element(*TestLocators.SEARCH_ACCOUNT_PROFILE).click()
        assert '/login' in driver.current_url

    def test_from_account_to_constructor(self, driver):
        driver.find_element(*TestLocators.SEARCH_ACCOUNT_PROFILE).click()
        driver.find_element(*TestLocators.SEARCH_NAME).send_keys(TestData.EMAIL_LOGIN)
        driver.find_element(*TestLocators.SEARCH_PASS).send_keys(TestData.PASSWORD)
        driver.find_element(*TestLocators.SEARCH_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_CHECKOUT))
        assert driver.find_element(*TestLocators.SEARCH_CHECKOUT), "Не удалось проверить переход к разделу"

    def test_from_account_to_logo(self, driver):
        driver.find_element(*TestLocators.SEARCH_ACCOUNT_PROFILE).click()
        driver.find_element(*TestLocators.SEARCH_NAME).send_keys(TestData.EMAIL_LOGIN)
        driver.find_element(*TestLocators.SEARCH_PASS).send_keys(TestData.PASSWORD)
        driver.find_element(*TestLocators.SEARCH_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_CHECKOUT))
        assert driver.find_element(*TestLocators.SEARCH_CHECKOUT), "Не удалось проверить переход к разделу"