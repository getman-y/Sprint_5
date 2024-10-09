from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locator
from tests.user import UserRegistration


class TestAuthorization:
    def test_auth_using_btn_login_to_account(self):
        user = UserRegistration()
        auth = user.registration_user_success()

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locator.BUTTON_LOGIN_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locator.REGISTRATION_EMAIL)).send_keys(auth.get('email'))
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(auth.get('password'))
        driver.find_element(*Locator.AUTH_BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.CREATE_ORDER_BUTTON))
        driver.find_element(*Locator.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.BUTTON_PROFILE))
        assert '/account/profile' in driver.current_url
        driver.quit()

    def test_auth_using_btn_account(self):
        user = UserRegistration()
        auth = user.registration_user_success()

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locator.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locator.REGISTRATION_EMAIL)).send_keys(auth.get('email'))
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(auth.get('password'))
        driver.find_element(*Locator.AUTH_BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.CREATE_ORDER_BUTTON))
        driver.find_element(*Locator.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.BUTTON_PROFILE))
        assert '/account/profile' in driver.current_url
        driver.quit()

    def test_auth_using_btn_login_on_registration_page(self):
        user = UserRegistration()
        auth = user.registration_user_success()

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*Locator.BUTTON_LOGIN_ON_REGISTRATION_PAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locator.REGISTRATION_EMAIL)).send_keys(auth.get('email'))
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(auth.get('password'))
        driver.find_element(*Locator.AUTH_BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.CREATE_ORDER_BUTTON))
        driver.find_element(*Locator.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.BUTTON_PROFILE))
        assert '/account/profile' in driver.current_url
        driver.quit()

    def test_auth_using_btn_login_on_forgot_password_page(self):
        user = UserRegistration()
        auth = user.registration_user_success()

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(*Locator.BUTTON_LOGIN_ON_FORGOT_PASSWORD_PAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locator.REGISTRATION_EMAIL)).send_keys(auth.get('email'))
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(auth.get('password'))
        driver.find_element(*Locator.AUTH_BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.CREATE_ORDER_BUTTON))
        driver.find_element(*Locator.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.BUTTON_PROFILE))
        assert '/account/profile' in driver.current_url
        driver.quit()
