from selenium.webdriver.common.by import By

class MainPageLocators:
    # Основные локаторы
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')] | //a[contains(text(), 'Войти')]")
    CREATE_ACC_BUTTON = (By.XPATH, "//a[contains(text(), 'Создать аккаунт')] | //button[contains(text(), 'Создать аккаунт')]")
    RECIPES_LABEL = (By.XPATH, "//h1[contains(text(), 'Рецепты')]")
    CREATE_RECIPET_BUTTON = (By.XPATH, "//a[contains(text(), 'Создать рецепт')] | //button[contains(text(), 'Создать рецепт')]")
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(text(), 'Выход')] | //button[contains(text(), 'Выход')]")    