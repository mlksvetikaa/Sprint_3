from tests.locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestToConstructor:
    def test_to_constructor_rolls(self, driver):
        driver.find_element(*TestLocators.SEARCH_SAUCES).click()
        driver.find_element(*TestLocators.SEARCH_ROLLS).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.ROLLS))
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.ROLLS_NAME))

    def test_to_constructor_sauces(self, driver):
        driver.find_element(*TestLocators.SEARCH_SAUCES).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SAUCES))
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SAUCES_NAME))

    def test_to_constructor_fillings(self, driver):
        driver.find_element(*TestLocators.SEARCH_FILLINGS).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.FILLINGS))
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.FILLINGS_NAME))