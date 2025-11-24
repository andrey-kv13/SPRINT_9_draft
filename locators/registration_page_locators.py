from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    REGISTRATION_LABEL = (By.XPATH, "//h1[text()='Регистрация']")
    FIRST_NAME_INPUT = (By.NAME, "first_name")
    LAST_NAME_INPUT = (By.NAME, "last_name")
    USERNAME_INPUT = (By.NAME, "username")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")