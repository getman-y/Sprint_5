from random import Random
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locator
from tests.constants import Constants
from user import UserRegistration


class TestRedirect:
    def test_redirect_to_account(self, driver):
        user = UserRegistration()
        auth = user.registration_user_success()

        driver.get(Constants.MAIN_PAGE_URL)
        driver.find_element(*Locator.BUTTON_LOGIN_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.AUTH_BUTTON_EXIT))
        driver.find_element(*Locator.REGISTRATION_EMAIL).send_keys(auth.get('email'))
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(auth.get('password'))
        driver.find_element(*Locator.AUTH_BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locator.BUTTON_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.BUTTON_PROFILE))
        assert '/account/profile' in driver.current_url

    def test_redirect_after_click_on_constructs(self, driver):
        user = UserRegistration()
        auth = user.registration_user_success()

        driver.get(Constants.MAIN_PAGE_URL)
        driver.find_element(*Locator.BUTTON_LOGIN_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.AUTH_BUTTON_EXIT))
        driver.find_element(*Locator.REGISTRATION_EMAIL).send_keys(auth.get('email'))
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(auth.get('password'))
        driver.find_element(*Locator.AUTH_BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locator.BUTTON_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locator.BUTTON_HEADER_CONSTRUCT)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.BUTTON_ACCOUNT))
        assert driver.find_element(*Locator.TITLE_MAKE_BURGER).text == 'Соберите бургер'

    def test_redirect_after_click_on_logo(self, driver):
        user = UserRegistration()
        auth = user.registration_user_success()

        driver.get(Constants.MAIN_PAGE_URL)
        driver.find_element(*Locator.BUTTON_LOGIN_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.AUTH_BUTTON_EXIT))
        driver.find_element(*Locator.REGISTRATION_EMAIL).send_keys(auth.get('email'))
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(auth.get('password'))
        driver.find_element(*Locator.AUTH_BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locator.BUTTON_ACCOUNT)).click()
        driver.find_element(*Locator.BUTTON_HEADER_LOGO).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.BUTTON_ACCOUNT))
        assert driver.find_element(*Locator.TITLE_MAKE_BURGER).text == 'Соберите бургер'
