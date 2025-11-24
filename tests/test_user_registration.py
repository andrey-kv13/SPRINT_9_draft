import allure
from config.config import Config

@allure.feature("Регистрация пользователя")
class TestUserRegistration:
    @allure.title("Тест: открытие страницы регистрации")
    @allure.description(
        "1. Открыть страницу регистрации.\n"
        "2. Проверить отображение заголовка и URL страницы."
    )
    def test_registration_page_is_opened(self, main_page, registration_page):
        """Тест проверяет, что страница регистрации открыта"""
        with allure.step("Открываем страницу регистрации"):
            main_page.click_create_acc_button()
            
        assert registration_page.get_registration_label_text() == "Регистрация"
        assert "signup" in registration_page.get_current_url(),\
        f'Страница регистрации не открыта, текущий URL: {registration_page.get_current_url()}'
    
    @allure.title("Тест: успешная регистрация нового пользователя")
    @allure.description(
        "1. Открыть страницу регистрации.\n"
        "2. Заполнить форму регистрации данными пользователя.\n"
        "3. Выполнить регистрацию и проверить переход на страницу входа."
    )
    def test_user_registration(self, registration_page, main_page, login_page):
        """Тест проверяет, что пользователь успешно зарегистрирован"""
        with allure.step("Открываем страницу регистрации"):
            main_page.click_create_acc_button()       
        with allure.step("Заполняем форму регистрации"):
            test_data = Config.test_data()
            registration_page.populate_registration_data(test_data["username"], test_data["password"])
        with allure.step("Ожидаем открытия страницы входа"):
            registration_page.wait_page_url("signin")
        with allure.step("Проверяем результат"):
            assert "signin" in registration_page.get_current_url(),\
                f'Страница входа не открыта, текущий URL: {registration_page.get_current_url()}'
            assert login_page.get_login_label_text() == "Войти на сайт",\
                f'Текст на странице входа не соответствует ожидаемому: {login_page.get_login_label_text()}'