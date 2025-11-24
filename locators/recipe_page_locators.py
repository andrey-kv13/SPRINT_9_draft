from selenium.webdriver.common.by import By

class RecipePageLocators:
    RECIPE_NAME_INPUT = (
        By.XPATH,
        ".//div[text()='Название рецепта']/following-sibling::input",
    )
    RECIPE_INGREDIENTS_INPUT = (
        By.XPATH,
        ".//div[text()='Ингредиенты']/following-sibling::input",
    )
    RECIPE_QUANTITY_INGREDIENT = (
        By.XPATH,
        ".//div[contains(@class, 'AmountInputContainer')]/descendant::input",
    )
    # Локатор для контейнера выпадающего списка ингредиентов
    INGREDIENT_DROPDOWN_CONTAINER = (
        By.XPATH,
        "//div[text()='Ингредиенты']/following-sibling::input/following::div[contains(@class, 'styles_container')][1]"
    )
    # Локатор для первого элемента выпадающего списка ингредиентов
    INGREDIENT_DROPDOWN_FIRST_ITEM = (
        By.XPATH,
        "//div[text()='Ингредиенты']/following-sibling::input/following::div[contains(@class, 'styles_container')][1]//div[1]"
    )
    RECIPE_ADD_INGREDIENT_BUTTON = (By.XPATH, ".//div[text()='Добавить ингредиент']")
    RECIPE_PREPARATION_TIME_INPUT = (By.XPATH,
        ".//div[text()='Время приготовления']/following-sibling::input",
    )
    RECIPE_DESCRIPTION_INPUT = (
        By.XPATH,
        ".//div[text()='Описание рецепта']/following-sibling::textarea",
    )
    RECIPE_LOGO_INPUT = (By.XPATH, ".//input[@type='file']")
    CREATE_RECIPE_BUTTON = (By.XPATH, "//button[text()='Создать рецепт']")
    RECEIPE_TITLE = (By.XPATH, "//h1")
    RECEIPE_CARD = (By.XPATH, "//img[@class='styles_single-card__image__O135K']")
