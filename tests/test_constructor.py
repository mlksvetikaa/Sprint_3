from tests.locators import TestLocators
import time


class TestToConstructor:
    def test_to_constructor_rolls(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_SAUCES).click()
        time.sleep(3)
        driver.find_element(*TestLocators.SEARCH_ROLLS).click()
        assert driver.find_element(*TestLocators.ROLLS).text == 'Булки'
        driver.quit()

    def test_to_constructor_sauces(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_SAUCES).click()
        assert driver.find_element(*TestLocators.SAUCES).text == 'Соусы'
        driver.quit()

    def test_to_constructor_fillings(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_FILLINGS).click()
        assert driver.find_element(*TestLocators.FILLINGS).text == 'Начинки'
        driver.quit()