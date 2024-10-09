from selenium.webdriver.common.by import By


class Locator:
    REGISTRATION_NAME = (By.XPATH, '//label[ text()="Имя" ]/parent::div/input')
    REGISTRATION_EMAIL = (By.XPATH, '//label[ text()="Email" ]/parent::div/input')
    REGISTRATION_PASSWORD = (By.XPATH, '//label[ text()="Пароль" ]/parent::div/input')
    REGISTRATION_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')
    AUTH_BUTTON_EXIT = (By.XPATH, './/button[text()="Войти"]')
    CREATE_ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')
    ERROR_MESSAGE_PASSWORD = (By.XPATH, './/p[text()="Некорректный пароль"]')
    BUTTON_LOGIN_TO_ACCOUNT = (By.XPATH, './/button[text()="Войти в аккаунт"]')
    BUTTON_ACCOUNT = (By.XPATH, './/p[text()="Личный Кабинет"]')
    BUTTON_LOGIN_ON_REGISTRATION_PAGE = (By.XPATH, './/p[text()="Личный Кабинет"]')
    PROFILE_BUTTON = (By.XPATH, './/a[text()="Войти"]')
    BUTTON_LOGIN_ON_FORGOT_PASSWORD_PAGE = (By.XPATH, './/a[text()="Войти"]')
    BUTTON_HEADER_CONSTRUCT = (By.XPATH, './/p[text()="Конструктор"]')
    BUTTON_HEADER_LOGO = (By.XPATH, './/a[starts-with(@href, "/")] ')
    BUTTON_LOGOUT = (By.XPATH, './/button[text()="Выход"]')
    CONSTRUCT_BUNS = (By.XPATH, './/span[text()="Булки"]')
    CONSTRUCT_SAUCES = (By.XPATH, './/span[text()="Соусы"]')
    CONSTRUCT_FILLINGS = (By.XPATH, './/span[text()="Начинки"]')
