from random import Random
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locator
from tests.constants import Constants


class UserRegistration:

    @staticmethod
    def registration_user_success():
        driver = webdriver.Chrome()
        random = Random()
        random_number = str(random.randint(1000, 9999))
        email = f'getman-yuliia{random_number}@yandex.ru'
        password = '123456'
        driver.get(Constants.REGISTER_URL)
        driver.find_element(*Locator.REGISTRATION_NAME).send_keys('Юля')
        driver.find_element(*Locator.REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*Locator.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locator.AUTH_BUTTON_EXIT))
        driver.find_element(*Locator.REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*Locator.AUTH_BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locator.BUTTON_ACCOUNT))
        driver.quit()
        return {'email': email, 'password': password}
