from faker import Faker
from config.paths import RECIPE_LOGO_PATH

fake = Faker()

class Config:
    """Конфигурация для тестов самокатов"""
    @staticmethod
    def test_data():
        return {
            "name": fake.first_name(),
            "last_name": fake.last_name(),
            "username": fake.user_name(),
            "email": fake.email(),
            "password": fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
        }
        
    BASE_URL = "https://foodgram-frontend-1.prakticum-team.ru/"
    TIMEOUT = 10
    # URL для Selenoid (используется при работе через Docker Compose)
    SELENOID_URI = "http://selenoid:4444/wd/hub"
    # Флаг для использования Remote WebDriver вместо локального
    USE_REMOTE_DRIVER = False
    NAME = fake.first_name()
    LAST_NAME = fake.last_name()
    USER_USERNAME = fake.user_name()
    EMAIL = fake.email()
    PASSWORD = fake.password(length=10, special_chars=True, 
                             digits=True, 
                             upper_case=True, 
                             lower_case=True)
    # Путь к логотипу рецепта (импортируется из config.paths)
    RECIPE_LOGO_PATH = RECIPE_LOGO_PATH