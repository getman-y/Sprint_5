from random import Random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locator


class TestAuthorization:
    def test_auth_using_btn_login_to_account(self):
        driver = webdriver.Chrome()
        random = Random()
        random_number = str(random.randint(1000, 9999))
        email = f'getmanyulia{random_number}@yandex.ru'
        password = '123456'
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*Locator.REGISTRATION_NAME).send_keys('Юля')
        driver.find_element(*Locator.REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*Locator.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))

        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locator.BUTTON_LOGIN_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))
        driver.find_element(*Locator.REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*Locator.AUTH_BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/p[text()="Личный Кабинет"]')))
        driver.find_element(*Locator.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/a[text()="Профиль"]')))
        assert '/account/profile' in driver.current_url
        driver.quit()

    def test_auth_using_btn_account(self):
        driver = webdriver.Chrome()
        random = Random()
        random_number = str(random.randint(1000, 9999))
        email = f'getmanyulia{random_number}@yandex.ru'
        password = '123456'
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*Locator.REGISTRATION_NAME).send_keys('Юля')
        driver.find_element(*Locator.REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*Locator.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))

        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locator.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))
        driver.find_element(*Locator.REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*Locator.AUTH_BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/p[text()="Личный Кабинет"]')))
        driver.find_element(*Locator.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/a[text()="Профиль"]')))
        assert '/account/profile' in driver.current_url
        driver.quit()

    def test_auth_using_btn_login_on_registration_page(self):
        driver = webdriver.Chrome()
        random = Random()
        random_number = str(random.randint(1000, 9999))
        email = f'getmanyulia{random_number}@yandex.ru'
        password = '123456'
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*Locator.REGISTRATION_NAME).send_keys('Юля')
        driver.find_element(*Locator.REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*Locator.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))

        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*Locator.BUTTON_LOGIN_ON_REGISTRATION_PAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))
        driver.find_element(*Locator.REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*Locator.AUTH_BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/p[text()="Личный Кабинет"]')))
        driver.find_element(*Locator.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/a[text()="Профиль"]')))
        assert '/account/profile' in driver.current_url
        driver.quit()

    def test_auth_using_btn_login_on_forgot_password_page(self):
        driver = webdriver.Chrome()
        random = Random()
        random_number = str(random.randint(1000, 9999))
        email = f'getmanyulia{random_number}@yandex.ru'
        password = '123456'
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*Locator.REGISTRATION_NAME).send_keys('Юля')
        driver.find_element(*Locator.REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*Locator.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))

        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(*Locator.BUTTON_LOGIN_ON_FORGOT_PASSWORD_PAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))
        driver.find_element(*Locator.REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*Locator.AUTH_BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/p[text()="Личный Кабинет"]')))
        driver.find_element(*Locator.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/a[text()="Профиль"]')))
        assert '/account/profile' in driver.current_url
        driver.quit()


test = TestAuthorization()
test.test_auth_using_btn_login_to_account()
test.test_auth_using_btn_account()
test.test_auth_using_btn_login_on_registration_page()
test.test_auth_using_btn_login_on_forgot_password_page()
