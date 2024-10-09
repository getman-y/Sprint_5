from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from user import UserRegistration
from locators import Locator


class TestLogout:
    def test_logout_success(self):
        user = UserRegistration()
        auth = user.registration_user_success()

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*Locator.REGISTRATION_EMAIL).send_keys(auth.get('email'))
        driver.find_element(*Locator.REGISTRATION_PASSWORD).send_keys(auth.get('password'))
        driver.find_element(*Locator.AUTH_BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locator.BUTTON_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.BUTTON_LOGOUT)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.AUTH_BUTTON_EXIT))
        assert '/login' in driver.current_url
        driver.quit()
