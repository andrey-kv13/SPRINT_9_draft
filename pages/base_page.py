from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.config import Config
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException

class BasePage:
    """Базовый класс с общими методами для работы со страницами"""
    
    def __init__(self, driver):
        self.driver = driver
        self.timeout = Config.TIMEOUT
        self.wait = WebDriverWait(driver, Config.TIMEOUT)
        
    def find_element(self, locator):
        """Поиск элемента с ожиданием его видимости"""       
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            return None
    
    def find_elements(self, locator):
        """Поиск всех элементов по локатору"""        
        try:
            elements = self.wait.until(EC.presence_of_all_elements_located(locator))
            return elements
        except TimeoutException:
            return []
    
    def find_element_by_presence(self, locator):
        """Поиск элемента по присутствию в DOM (не требует видимости)"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            return None

    def scroll_to_element(self, locator):
        """Скролл к указанному элементу"""     
        element = self.find_element(locator)
        if element is not None:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        else:
            raise TimeoutException(f"Элемент не найден для скролла: {locator}")

    def click(self, locator):
        """Клик по элементу со скроллом и ожиданием кликабельности"""   
        try:
            # Сначала находим элемент и проверяем его наличие
            element = self.wait.until(EC.presence_of_element_located(locator))
            if element is None:
                # Пытаемся найти элемент через альтернативные методы
                try:
                    element = self.driver.find_element(*locator)
                except NoSuchElementException:
                    current_url = self.driver.current_url
                    page_source_snippet = self.driver.page_source[:500] if len(self.driver.page_source) > 500 else self.driver.page_source
                    raise TimeoutException(
                        f"Элемент не найден: {locator}\n"
                        f"Текущий URL: {current_url}\n"
                        f"Фрагмент страницы: {page_source_snippet}"
                    )
            # Скроллим к элементу
            try:
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            except Exception:
                pass  # Продолжаем даже если скролл не удался
            # Ждем, пока элемент станет кликабельным
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except (TimeoutException, ElementClickInterceptedException) as e:
            # Если обычный клик не работает, используем JavaScript клик
            try:
                element = self.wait.until(EC.presence_of_element_located(locator))
                self.driver.execute_script("arguments[0].click();", element)
            except TimeoutException:
                current_url = self.driver.current_url
                raise TimeoutException(
                    f"Элемент не найден для клика: {locator}\n"
                    f"Текущий URL: {current_url}\n"
                    f"Оригинальная ошибка: {str(e)}"
                )
    
    def click_with_js(self, locator):
        """Клик по элементу через JavaScript (обходит перехват клика)"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)
    
    def send_keys(self, locator, text):
        """Ввод текста в поле"""
        try:
            element = self.find_element(locator)
            if element is None:
                raise TimeoutException(f"Элемент не найден для ввода текста: {locator}")
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            raise TimeoutException(f"Не удалось ввести текст в элемент: {locator}")
    
    def get_element_text(self, locator):
        try:
            element = self.find_element(locator)
            if element is None:
                return None
            return element.text
        except TimeoutException:
            return None
    
    def get_attribute(self, locator, attribute):
        try:
            element = self.find_element(locator)
            if element is None:
                return None
            return element.get_attribute(attribute)
        except TimeoutException:
            return None
    
    def wait_page_url(self, url_part):
        """Ожидает, пока не откроется страница с указанной частью URL"""
        try:
            self.wait.until(EC.url_contains(url_part))
        except TimeoutException:
            return False
        return True
    
    def wait_page_url_not_contains(self, url_part):
        """Ожидает, пока URL не перестанет содержать указанную часть"""
        try:
            self.wait.until(lambda driver: url_part not in driver.current_url)
        except TimeoutException:
            return False
        return True
    
    def wait_element_invisible(self, locator):
        """Ожидает, пока элемент не станет невидимым"""
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def get_current_url(self):
        """Получает текущий URL страницы"""
        return self.driver.current_url
    
    def select_first_dropdown_item(self, dropdown_item_locator, dropdown_container_locator=None):
        """Выбирает первый элемент из выпадающего списка"""
        # Если передан локатор контейнера, ждем его появления
        if dropdown_container_locator:
            self.find_element(dropdown_container_locator)
        self.click(dropdown_item_locator)