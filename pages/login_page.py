from locators.login_page_locators import LoginPageLocators as lpl
from pages.base_page import BasePage

class LoginPage(BasePage):
    
    def __init__(self, driver):
        """Инициализирует страницу входа"""
        super().__init__(driver)
    
    def get_login_label_text(self):
        """Получает текст заголовка страницы входа"""
        return self.get_element_text(lpl.LOGIN_LABEL)
    
    def click_login_button(self):
        self.click(lpl.LOGIN_BUTTON)
    
    def populate_login_data(self, user_name, password):
        """Заполняет форму входа данными пользователя"""
        self.wait_page_url("signin")
        self.send_keys(lpl.EMAIL_INPUT, user_name)
        self.send_keys(lpl.PASSWORD_INPUT, password)
        self.click(lpl.LOGIN_BUTTON)