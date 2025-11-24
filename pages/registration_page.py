from locators.registration_page_locators import RegistrationPageLocators as rpl
from pages.base_page import BasePage
from config.config import Config

class RegistrationPage(BasePage):
    
    def __init__(self, driver):
        """Инициализирует страницу регистрации"""
        super().__init__(driver)
        
    def click_create_button(self):
        """Нажимает на кнопку 'Создать аккаунт'"""
        self.click(rpl.REGISTER_BUTTON)
        
    def populate_registration_data(self, user_name, password, test_data=None):
        """Заполняет форму регистрации данными пользователя"""
        if test_data is None:
            test_data = Config.test_data()
        self.send_keys(rpl.FIRST_NAME_INPUT, test_data["name"])
        self.send_keys(rpl.LAST_NAME_INPUT, test_data["last_name"])
        self.send_keys(rpl.USERNAME_INPUT, user_name)
        self.send_keys(rpl.EMAIL_INPUT, test_data["email"])
        self.send_keys(rpl.PASSWORD_INPUT, password)
        self.click(rpl.REGISTER_BUTTON)
        
    def get_registration_label_text(self):
        """Получает текст заголовка страницы регистрации"""
        return self.get_element_text(rpl.REGISTRATION_LABEL)