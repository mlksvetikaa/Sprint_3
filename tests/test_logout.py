from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.data import TestData
from tests.locators import TestLocators


def test_to_account(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*TestLocators.SEARCH_LOGIN_ACCOUNT).click()
    driver.find_element(*TestLocators.SEARCH_NAME).send_keys(TestData.EMAIL_LOGIN)
    driver.find_element(*TestLocators.SEARCH_PASS).send_keys(TestData.PASSWORD)
    driver.find_element(*TestLocators.SEARCH_LOGIN).click()
    WebDriverWait(driver, 5).until(
         expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ACCOUNT_PROFILE))
    driver.find_element(*TestLocators.SEARCH_ACCOUNT_PROFILE).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(TestLocators.SEARCH_LOGOUT))
    driver.find_element(*TestLocators.SEARCH_LOGOUT).click()
    WebDriverWait(driver, 7).until(
        expected_conditions.visibility_of_element_located(TestLocators.SEARCH_LOGIN))
    assert driver.find_element(*TestLocators.SEARCH_LOGIN), "Не удалось выйти из аккаунта в личном кабинете"

    driver.quit()