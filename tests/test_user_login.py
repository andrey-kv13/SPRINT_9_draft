import allure

@allure.feature("Авторизация пользователя")
class TestUserLogin:
    @allure.title("Тест: открытие страницы входа")
    @allure.description(
        "1. Открыть страницу входа.\n"
        "2. Проверить отображение заголовка и URL страницы."
    )
    def test_login_page_is_opened(self, main_page, login_page):
        """Тест проверяет, что страница входа открыта"""
        with allure.step("Открываем страницу входа"):
            main_page.click_login_button()
        with allure.step("Проверяем результат"):
            assert login_page.get_login_label_text() == "Войти на сайт"
            assert "signin" in login_page.get_current_url(),\
            f'Страница входа не открыта, текущий URL: {login_page.get_current_url()}'
    
    @allure.title("Тест: успешный вход авторизованного пользователя")
    @allure.description(
        "1. Зарегистрировать пользователя.\n"
        "2. Заполнить форму входа и выполнить авторизацию.\n"
        "3. Проверить переход на главную страницу и отображение рецептов."
    )
    def test_user_login(self, login_page, base_page, main_page, registered_user):
        """Тест проверяет, что пользователь успешно вошел в систему"""
        user_name, password =  registered_user
        with allure.step("Заполняем форму входа"):
            login_page.populate_login_data(user_name, password)
        with allure.step("Ожидаем перехода на главную страницу"):
            base_page.wait_page_url("recipes")
        with allure.step("Проверяем результат"):
            assert "signin" not in login_page.get_current_url(),\
            f'Страница входа не открыта, текущий URL: {login_page.get_current_url()}'
            assert main_page.get_recipes_label_text() == "Рецепты"
            assert main_page.is_logout_button_displayed(), "Кнопка 'Выход' не отображается"