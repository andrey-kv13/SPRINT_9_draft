from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    CREATE_ACC_BUTTON = (By.XPATH, "//a[text()='Создать аккаунт']")
    RECIPES_LABEL = (By.XPATH, "//h1[text()='Рецепты']")
    CREATE_RECIPET_BUTTON = (By.XPATH, "//a[text()='Создать рецепт']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Выход']")    