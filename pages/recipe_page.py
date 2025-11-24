from pages.base_page import BasePage
from locators.recipe_page_locators import RecipePageLocators as recipe_locators
from config.config import Config
from pathlib import Path

class RecipePage(BasePage):
    
    def select_ingredient(self, first_ingredient, second_ingredient):
        """Выбирает ингредиенты для рецепта"""
        # Выбираем первый ингредиент
        self.send_keys(recipe_locators.RECIPE_INGREDIENTS_INPUT, first_ingredient)
        self.select_first_dropdown_item(
            recipe_locators.INGREDIENT_DROPDOWN_FIRST_ITEM,
            recipe_locators.INGREDIENT_DROPDOWN_CONTAINER
        )
        # Кликаем по полю количества, чтобы закрыть выпадающий список
        self.click(recipe_locators.RECIPE_QUANTITY_INGREDIENT)
        self.send_keys(recipe_locators.RECIPE_QUANTITY_INGREDIENT, "100")
        # Используем JavaScript клик для кнопки, чтобы избежать перехвата
        self.click_with_js(recipe_locators.RECIPE_ADD_INGREDIENT_BUTTON)
        
        # Выбираем второй ингредиент
        self.send_keys(recipe_locators.RECIPE_INGREDIENTS_INPUT, second_ingredient)
        self.select_first_dropdown_item(
            recipe_locators.INGREDIENT_DROPDOWN_FIRST_ITEM,
            recipe_locators.INGREDIENT_DROPDOWN_CONTAINER
        )
        # Кликаем по полю количества, чтобы закрыть выпадающий список
        self.click(recipe_locators.RECIPE_QUANTITY_INGREDIENT)
        self.send_keys(recipe_locators.RECIPE_QUANTITY_INGREDIENT, "100")
        # Используем JavaScript клик для кнопки, чтобы избежать перехвата
        self.click_with_js(recipe_locators.RECIPE_ADD_INGREDIENT_BUTTON)
        
    def select_recipe_logo(self, logo_path=None):
        """Выбирает логотип рецепта"""
        if logo_path is None:
            # Получаем абсолютный путь к файлу через pathlib
            logo_path = Path(Config.RECIPE_LOGO_PATH).resolve()
        else:
            # Если передан путь, преобразуем его в Path и получаем абсолютный путь
            logo_path = Path(logo_path).resolve()
        
        # Проверяем, что файл существует
        if not logo_path.exists():
            raise FileNotFoundError(f"Файл не найден: {logo_path}")
        
        # Используем find_element_by_presence, так как input[type='file'] может быть скрыт
        file_input = self.find_element_by_presence(recipe_locators.RECIPE_LOGO_INPUT)
        if file_input is None:
            raise Exception("Элемент input[type='file'] не найден на странице")
        
        # Преобразуем Path в строку для send_keys (абсолютный путь)
        file_input.send_keys(str(logo_path))
        
    def populate_recipe_data(self, recipe_name):
        """Заполняет данные рецепта и создает его"""
        self.send_keys(recipe_locators.RECIPE_NAME_INPUT, recipe_name)
        self.select_ingredient("багет", "сосиски")
        self.send_keys(recipe_locators.RECIPE_PREPARATION_TIME_INPUT, "10")
        self.send_keys(recipe_locators.RECIPE_DESCRIPTION_INPUT, "Тестовое описание рецепта")
        self.select_recipe_logo()
        self.click(recipe_locators.CREATE_RECIPE_BUTTON)
        # Ждем, пока страница перезагрузится и URL изменится (убедимся, что "create" исчезнет из URL)
        self.wait_page_url_not_contains("create")
        # Дополнительно ждем появления карточки рецепта
        self.find_element(recipe_locators.RECEIPE_CARD)
        return recipe_name
    
    def get_recipe_title(self):
        """Получает название рецепта"""
        return self.get_element_text(recipe_locators.RECEIPE_TITLE)
    
    def is_recipe_card_displayed(self):
        """Проверяет, отображается ли карточка рецепта"""
        element = self.find_element(recipe_locators.RECEIPE_CARD)
        return element is not None
