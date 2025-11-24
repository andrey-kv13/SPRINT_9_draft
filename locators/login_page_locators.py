from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_LABEL = (By.XPATH, "//h1[text()='Войти на сайт']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")