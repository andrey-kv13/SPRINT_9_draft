from selenium import webdriver
import pytest
import os
from config.config import Config
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.recipe_page import RecipePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации WebDriver"""
    use_remote = os.getenv("USE_REMOTE_DRIVER", "false").lower() == "true"

    if use_remote:
        # Используем Remote WebDriver для работы с Selenoid в Docker
        selenoid_uri = os.getenv("SELENOID_URI", Config.SELENOID_URI)
        options = ChromeOptions()
        options.add_argument("--incognito")
        
        driver = webdriver.Remote(
            command_executor=selenoid_uri,
            options=options
        )
    else:
        # Используем локальный Chrome WebDriver
        options = ChromeOptions()
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)

    # Отключаем неявные ожидания - используем только явные ожидания
    driver.implicitly_wait(0)
    driver.maximize_window()
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def main_page(driver):
    return MainPage(driver)

@pytest.fixture(scope="function")
def registration_page(driver):
    return RegistrationPage(driver)

@pytest.fixture(scope="function")
def base_page(driver):
    return BasePage(driver)

@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture(scope="function")
def recipe_page(driver):
    return RecipePage(driver)

@pytest.fixture(scope="function")
def registered_user(main_page, registration_page):
    """Фикстура для регистрации пользователя. Возвращает данные пользователя."""
    test_data = Config.test_data()
    user_name = test_data["username"]
    password = test_data["password"]
    main_page.click_create_acc_button()
    registration_page.populate_registration_data(user_name, password, test_data)
    registration_page.wait_page_url("signin")
    return user_name, password

@pytest.fixture(scope="function")
def logged_in_user(registered_user, login_page, base_page, main_page):
    """Фикстура для авторизации пользователя. Выполняет регистрацию и вход."""
    user_name, password = registered_user
    login_page.populate_login_data(user_name, password)
    base_page.wait_page_url("recipes")
    main_page.find_element(MainPageLocators.RECIPES_LABEL)
    return registered_user