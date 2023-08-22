import random
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.data import TestData
from tests.locators import TestLocators


class TestRegistration:
    def test_registration(self, driver):
        driver.find_element(*TestLocators.SEARCH_LOGIN_ACCOUNT).click()
        driver.find_element(*TestLocators.SEARCH_REGISTER).click()
        driver.find_element(*TestLocators.SEARCH_NAME_REGISTRATION).send_keys(TestData.NAME_REGISTRATION)
        new_email = f"svetlanavasileva12{random.randint(100, 999)}@yandex.ru"
        driver.find_element(*TestLocators.SEARCH_EMAIL_REGISTRATION).send_keys(new_email)
        driver.find_element(*TestLocators.SEARCH_PASS).send_keys(TestData.PASSWORD)
        driver.find_element(*TestLocators.SEARCH_BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN))
        assert driver.find_element(*TestLocators.LOGIN), "Не удалось пройти регистрацию"

    def test_registration_incorrect_password(self, driver):
        driver.find_element(*TestLocators.SEARCH_LOGIN_ACCOUNT).click()
        driver.find_element(*TestLocators.SEARCH_REGISTER).click()
        driver.find_element(*TestLocators.SEARCH_NAME_REGISTRATION).send_keys(TestData.NAME_REGISTRATION)
        new_email = f"svetlanavasileva12{random.randint(100, 999)}@yandex.ru"
        driver.find_element(*TestLocators.SEARCH_EMAIL_REGISTRATION).send_keys(new_email)
        driver.find_element(*TestLocators.SEARCH_PASS).send_keys('123')
        driver.find_element(*TestLocators.SEARCH_BUTTON_REGISTRATION).click()
        assert driver.find_element(*TestLocators.INCORRECT_PASSWORD), "Проверка не прошла"