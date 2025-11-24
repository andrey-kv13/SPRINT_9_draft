import allure

@allure.feature("Создание рецепта")
class TestCreateRecipe:
    @allure.title("Тест: успешное создание рецепта авторизованным пользователем")
    @allure.description(
        "1. Авторизоваться и перейти на таб 'Создать рецепт'.\n"
        "2. Заполнить все поля формы создания рецепта и нажать кнопку 'Создать рецепт'.\n"
        "3. Проверить отображение карточки и совпадение названия."
    )
    def test_create_recipe(self, main_page, recipe_page, logged_in_user):
        """Тест проверяет, что пользователь может создать рецепт"""    
        with allure.step("Открываем страницу создания рецепта"):
            main_page.click_create_recipe_button()
        with allure.step("Заполняем форму создания рецепта"):
           recipe_name = recipe_page.populate_recipe_data("Тестовый рецепт")
        with allure.step("Проверяем результат"):
            assert recipe_page.is_recipe_card_displayed(), "Карточка созданного рецепта не отображается"
            assert recipe_page.get_recipe_title() == recipe_name,\
                f"Название рецепта не совпадает. Ожидалось: '{recipe_name}', найдено: '{recipe_page.get_recipe_title()}'"
            assert "create" not in recipe_page.get_current_url(),\
            f'Страница с созданным рецептом не открыта, текущий URL: {recipe_page.get_current_url()}'