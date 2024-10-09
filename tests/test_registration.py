from random import Random
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locator


class TestRegistration:
    def test_registration_success(self):
        driver = webdriver.Chrome()
        random = Random()
        random_number = str(random.randint(1000, 9999))
        email = f'getmanyuliia{random_number}@yandex.ru'
        password = '123456'
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*Locator.REGISTRATION_NAME).send_keys('Юля')
        driver.find_element(*Locator.REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*Locator.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.AUTH_BUTTON_EXIT))
        driver.find_element(*Locator.REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*Locator.AUTH_BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.CREATE_ORDER_BUTTON))
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_registration_wrong_password(self):
        driver = webdriver.Chrome()
        random = Random()
        random_number = str(random.randint(1000, 9999))
        email = f'getmanyuliia{random_number}@yandex.ru'
        password = '12345'

        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*Locator.REGISTRATION_NAME).send_keys('Юля')
        driver.find_element(*Locator.REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*Locator.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locator.ERROR_MESSAGE_PASSWORD))
        assert driver.find_element(*Locator.ERROR_MESSAGE_PASSWORD).text == 'Некорректный пароль'
        driver.quit()
