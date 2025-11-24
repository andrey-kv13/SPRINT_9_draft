# Автоматизированное тестирование веб-приложения Foodgram

Проект содержит автоматизированные тесты для веб-приложения Foodgram, написанные на Python с использованием Selenium WebDriver и паттерна Page Object Model.

## Структура проекта

```
Sprint_9/
├── assets/                    # Ресурсы проекта (изображения)
│   └── recipe_logo.jpeg
├── config/                    # Конфигурация проекта
│   ├── config.py             # Настройки и тестовые данные
│   └── paths.py              # Пути к ресурсам
├── helpers/                   # Вспомогательные классы
│   └── user_helper.py        # Хелпер для работы с пользователями
├── locators/                  # Локаторы элементов страниц
│   ├── login_page_locators.py
│   ├── main_page_locators.py
│   ├── recipe_page_locators.py
│   └── registration_page_locators.py
├── pages/                     # Page Object классы
│   ├── base_page.py          # Базовый класс для всех страниц
│   ├── login_page.py
│   ├── main_page.py
│   ├── recipe_page.py
│   └── registration_page.py
├── tests/                     # Тестовые сценарии
│   ├── test_create_recipe.py
│   ├── test_user_login.py
│   └── test_user_registration.py
├── .github/
│   └── workflows/
│       └── ci.yml            # CI/CD конфигурация для GitHub Actions
├── browser.json               # Конфигурация браузеров для Selenoid
├── conftest.py                # Фикстуры pytest
├── docker-compose.yml         # Конфигурация Docker Compose
├── Dockerfile                 # Docker образ для тестов
├── pytest.ini                # Конфигурация pytest
└── requirements.txt           # Зависимости проекта
```

## Тестовые сценарии

### 1. Создание аккаунта
- Нажатие кнопки «Создать аккаунт»
- Заполнение всех полей формы регистрации
- Проверка перехода на страницу авторизации и отображения формы авторизации

### 2. Авторизация
- Нажатие кнопки «Войти»
- Заполнение всех полей формы авторизации
- Проверка перехода на главную страницу и отображения кнопки «Выход»

### 3. Создание рецепта
- Авторизация и переход на таб «Создать рецепт»
- Заполнение всех полей формы создания рецепта (включая добавление ингредиентов из списка)
- Проверка отображения карточки созданного рецепта и совпадения названия

## Установка и настройка

### Требования
- Python 3.11+
- pip
- Docker и Docker Compose (для запуска через Selenoid)
- Allure Framework (для генерации отчетов)

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Установка Allure

**Windows:**
```bash
# Скачать и распаковать Allure из https://github.com/allure-framework/allure2/releases
# Добавить в PATH
```

**Linux/Mac:**
```bash
# Через Homebrew (Mac)
brew install allure

# Или скачать вручную
wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.9/allure-commandline-2.13.9.zip
unzip allure-commandline-2.13.9.zip
sudo mv allure-2.13.9 /opt/allure
sudo ln -s /opt/allure/bin/allure /usr/local/bin/allure
```

## Запуск тестов

### Локальный запуск

```bash
# Запуск всех тестов
pytest tests/

# Запуск с генерацией Allure результатов
pytest --alluredir=allure-results tests/

# Запуск конкретного теста
pytest tests/test_user_registration.py
```

### Запуск через Docker Compose

1. Запустить Selenoid:
```bash
docker-compose up -d
```

2. Настроить использование Remote WebDriver в `config/config.py`:
```python
USE_REMOTE_DRIVER = True
```

Или через переменную окружения:
```bash
set USE_REMOTE_DRIVER=true  # Windows
export USE_REMOTE_DRIVER=true  # Linux/Mac
```

3. Запустить тесты:
```bash
pytest --alluredir=allure-results tests/
```

### Запуск через Docker

```bash
# Сборка образа
docker build -t foodgram-tests .

# Запуск тестов в контейнере
docker run --rm -v %cd%/allure-results:/app/allure-results foodgram-tests
```

## Генерация Allure отчетов

### Генерация отчета

```bash
# Генерация отчета из результатов
allure generate allure-results -o allure-report --clean

# Открытие отчета в браузере
allure open allure-report
```

### Публикация отчета

После генерации отчета, папка `allure-report/` должна быть закоммичена в репозиторий для просмотра результатов тестирования.

## CI/CD

Проект настроен для работы с GitHub Actions. При каждом push в ветки `main` или `master` автоматически:
1. Запускается Selenoid
2. Выполняются все тесты
3. Генерируется Allure отчет
4. Отчет загружается как артефакт

Конфигурация находится в `.github/workflows/ci.yml`.

## Конфигурация

Основные настройки находятся в `config/config.py`:
- `BASE_URL` - базовый URL тестируемого приложения
- `BROWSER` - браузер для тестов (Chrome/Firefox)
- `TIMEOUT` - таймаут ожидания элементов
- `USE_REMOTE_DRIVER` - использование Remote WebDriver (для Selenoid)

Тестовые данные генерируются автоматически с помощью библиотеки Faker через метод `Config.test_data()`.

## Структура тестов

Тесты организованы по функциональности:
- `test_user_registration.py` - тесты регистрации пользователя
- `test_user_login.py` - тесты авторизации пользователя
- `test_create_recipe.py` - тесты создания рецепта

Каждый тест независим и использует фикстуры из `conftest.py` для настройки окружения.

## Page Object Model

Проект использует паттерн Page Object Model:
- Каждая страница имеет свой класс в `pages/`
- Локаторы вынесены в отдельные файлы в `locators/`
- Общая функциональность находится в `BasePage`
- Вспомогательные методы для работы с пользователями в `helpers/`

## Зависимости

Основные библиотеки:
- `selenium==4.15.2` - автоматизация браузера
- `pytest==7.4.3` - фреймворк для тестирования
- `allure-pytest==2.13.2` - интеграция Allure с pytest
- `faker==20.1.0` - генерация тестовых данных

Полный список зависимостей в `requirements.txt`.

## Примечания

- Для работы с ингредиентами в форме создания рецепта необходимо начать вводить название ингредиента в поле ввода для отображения списка
- Все тесты используют явные ожидания (WebDriverWait) вместо неявных
- Тестовые данные генерируются случайным образом для каждого запуска
- Для работы через Selenoid необходимо запустить `docker-compose up -d` перед запуском тестов

## Автор

Проект создан в рамках Sprint 9 курса автоматизации тестирования.

#   S p r i n t _ 9  
 #   S P R I N T _ 9 _ d r a f t  
 