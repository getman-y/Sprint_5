from random import Random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locator


class TestConstruct:
    def test_construct_tab_buns(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locator.CONSTRUCT_FILLINGS).click()
        driver.find_element(*Locator.CONSTRUCT_BUNS).click()
        assert driver.find_element(By.XPATH, "//div/ul[1]/a[1]/p[1]").text == 'Флюоресцентная булка R2-D3'
        driver.quit()

    def test_construct_tab_fillings(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locator.CONSTRUCT_FILLINGS).click()
        assert driver.find_element(By.XPATH, "//div/ul[3]/a[1]/p[1]").text == 'Мясо бессмертных моллюсков Protostomia'
        driver.quit()

    def test_construct_tab_sauces(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locator.CONSTRUCT_SAUCES).click()
        time.sleep(2)
        assert driver.find_element(By.XPATH, "//div/ul[2]/a[1]/p[1]").text == 'Соус Spicy-X'
        driver.quit()


test = TestConstruct()
test.test_construct_tab_buns()
test.test_construct_tab_fillings()
test.test_construct_tab_sauces()

