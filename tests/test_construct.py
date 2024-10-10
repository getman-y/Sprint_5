from selenium import webdriver
from locators import Locator
from tests.constants import Constants


class TestConstruct:
    def test_construct_tab_buns(self, driver):
        driver.get(Constants.MAIN_PAGE_URL)
        driver.find_element(*Locator.CONSTRUCT_FILLINGS).click()
        driver.find_element(*Locator.CONSTRUCT_BUNS).click()
        assert driver.find_element(*Locator.NAME_OF_BUNS).text == 'Флюоресцентная булка R2-D3'

    def test_construct_tab_fillings(self, driver):
        driver.get(Constants.MAIN_PAGE_URL)
        driver.find_element(*Locator.CONSTRUCT_FILLINGS).click()
        assert driver.find_element(*Locator.NAME_OF_FILLINGS).text == 'Мясо бессмертных моллюсков Protostomia'

    def test_construct_tab_sauces(self, driver):
        driver.get(Constants.MAIN_PAGE_URL)
        driver.find_element(*Locator.CONSTRUCT_SAUCES).click()
        assert driver.find_element(*Locator.NAME_OF_SAUCES).text == 'Соус Spicy-X'
