"""
Модуль для хранения путей к ресурсам проекта (изображения, файлы и т.д.)
Все пути вычисляются относительно корня проекта для кроссплатформенной совместимости
"""
from pathlib import Path

# Получаем путь к корню проекта (директория, где находится config)
# Используем parent.parent, так как этот файл находится в config/, а корень проекта на уровень выше
PROJECT_ROOT = Path(__file__).parent.parent

# Пути к ресурсам
ASSETS_DIR = PROJECT_ROOT / "assets"
RECIPE_LOGO_PATH = str(ASSETS_DIR / "recipe_logo.jpeg")

