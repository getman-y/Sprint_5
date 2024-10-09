from random import Random
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locator


class UserRegistration:

    @staticmethod
    def registration_user_success():
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
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))
        driver.find_element(*Locator.REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*Locator.AUTH_BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/p[text()="Личный Кабинет"]')))
        driver.quit()
        return {'email': email, 'password': password}
