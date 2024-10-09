from selenium import webdriver
from locators import Locator


class TestConstruct:
    def test_construct_tab_buns(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locator.CONSTRUCT_FILLINGS).click()
        driver.find_element(*Locator.CONSTRUCT_BUNS).click()
        assert driver.find_element(*Locator.NAME_OF_BUNS).text == 'Флюоресцентная булка R2-D3'
        driver.quit()

    def test_construct_tab_fillings(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locator.CONSTRUCT_FILLINGS).click()
        assert driver.find_element(*Locator.NAME_OF_FILLINGS).text == 'Мясо бессмертных моллюсков Protostomia'
        driver.quit()

    def test_construct_tab_sauces(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locator.CONSTRUCT_SAUCES).click()
        assert driver.find_element(*Locator.NAME_OF_SAUCES).text == 'Соус Spicy-X'
        driver.quit()
