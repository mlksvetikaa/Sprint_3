from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.data import TestData
from tests.locators import TestLocators


class TestLogin:
    def test_login_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_LOGIN_ACCOUNT).click()
        driver.find_element(*TestLocators.SEARCH_NAME).send_keys(TestData.EMAIL_LOGIN)
        driver.find_element(*TestLocators.SEARCH_PASS).send_keys(TestData.PASSWORD)
        driver.find_element(*TestLocators.SEARCH_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_CHECKOUT))
        assert driver.find_element(*TestLocators.SEARCH_CHECKOUT), "Не удалось войти в аккаунт"
        driver.quit()

    def test_login_account_profile(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_ACCOUNT_PROFILE).click()
        driver.find_element(*TestLocators.SEARCH_NAME).send_keys(TestData.EMAIL_LOGIN)
        driver.find_element(*TestLocators.SEARCH_PASS).send_keys(TestData.PASSWORD)
        driver.find_element(*TestLocators.SEARCH_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_CHECKOUT))
        assert driver.find_element(*TestLocators.SEARCH_CHECKOUT), "Не удалось войти в аккаунт"
        driver.quit()

    def test_login_form_registration(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_LOGIN_ACCOUNT).click()
        driver.find_element(*TestLocators.SEARCH_REGISTER).click()
        driver.find_element(*TestLocators.SEARCH_REGISTER_LOGIN).click()
        driver.find_element(*TestLocators.SEARCH_NAME).send_keys(TestData.EMAIL_LOGIN)
        driver.find_element(*TestLocators.SEARCH_PASS).send_keys(TestData.PASSWORD)
        driver.find_element(*TestLocators.SEARCH_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_CHECKOUT))
        assert driver.find_element(*TestLocators.SEARCH_CHECKOUT), "Не удалось войти в аккаунт"
        driver.quit()

    def test_login_form_restore(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_LOGIN_ACCOUNT).click()
        driver.find_element(*TestLocators.SEARCH_RESTORE).click()
        driver.find_element(*TestLocators.SEARCH_REGISTER_LOGIN).click()
        driver.find_element(*TestLocators.SEARCH_NAME).send_keys(TestData.EMAIL_LOGIN)
        driver.find_element(*TestLocators.SEARCH_PASS).send_keys(TestData.PASSWORD)
        driver.find_element(*TestLocators.SEARCH_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_CHECKOUT))
        assert driver.find_element(*TestLocators.SEARCH_CHECKOUT), "Не удалось войти в аккаунт"
        driver.quit()