import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from config.config import Config
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.recipe_page import RecipePage


@pytest.fixture(scope="session")
def driver():
    """Создает и настраивает WebDriver"""
    use_remote = os.getenv("USE_REMOTE_DRIVER", "false").lower() == "true"
    selenoid_uri = os.getenv("SELENOID_URI", Config.SELENOID_URI)
    
    if use_remote:
        # Используем Remote WebDriver для Selenoid
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        
        driver = webdriver.Remote(
            command_executor=selenoid_uri,
            options=chrome_options
        )
    else:
        # Используем локальный WebDriver
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        
        driver = webdriver.Chrome(options=chrome_options)
    
    driver.maximize_window()
    driver.get(Config.BASE_URL)
    
    yield driver
    
    driver.quit()


@pytest.fixture
def base_page(driver):
    """Фикстура для базовой страницы"""
    return BasePage(driver)


@pytest.fixture
def main_page(driver):
    """Фикстура для главной страницы"""
    page = MainPage(driver)
    driver.get(Config.BASE_URL)
    # Ждем загрузки страницы
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import TimeoutException
    wait = WebDriverWait(driver, Config.TIMEOUT)
    try:
        # Ждем, пока страница загрузится (проверяем наличие body или любого элемента)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        # Даем дополнительное время для загрузки JavaScript
        import time
        time.sleep(2)
    except TimeoutException:
        pass  # Продолжаем даже если ожидание не сработало
    return page


@pytest.fixture
def login_page(driver):
    """Фикстура для страницы входа"""
    return LoginPage(driver)


@pytest.fixture
def registration_page(driver):
    """Фикстура для страницы регистрации"""
    return RegistrationPage(driver)


@pytest.fixture
def recipe_page(driver):
    """Фикстура для страницы создания рецепта"""
    return RecipePage(driver)


@pytest.fixture
def registered_user(main_page, registration_page):
    """Фикстура для зарегистрированного пользователя"""
    test_data = Config.test_data()
    username = test_data["username"]
    password = test_data["password"]
    
    # Открываем страницу регистрации
    main_page.click_create_acc_button()
    # Регистрируем пользователя
    registration_page.populate_registration_data(username, password, test_data)
    # Ждем перехода на страницу входа
    registration_page.wait_page_url("signin")
    
    return username, password


@pytest.fixture
def logged_in_user(main_page, login_page, registered_user):
    """Фикстура для авторизованного пользователя"""
    username, password = registered_user
    
    # Открываем страницу входа
    main_page.click_login_button()
    # Авторизуемся
    login_page.populate_login_data(username, password)
    # Ждем перехода на главную страницу
    login_page.wait_page_url("recipes")
    
    return username, password

