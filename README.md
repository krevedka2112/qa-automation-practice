# Автоматизация тестирования (UI & API)

Репозиторий содержит учебный фреймворк для автоматизации UI-тестов (авторизация) и API-тестов (эндпоинты объектов) с использованием **Pytest** и **Playwright**.

## Технологический стек
* **Язык**: Python 3.12
* **Тест-раннер**: Pytest

---

## Локальное развертывание и запуск

### 1. Подготовка окружения
Склонируйте репозиторий и перейдите в корневую папку проекта:
```
git clone https://github.com/krevedka2112/qa-automation-practice.git
cd qa-automation-practice
```
Создайте и активируйте виртуальное окружение:
```
python3.12 -m venv venv
source venv/bin/activate
```

### 2. Установка зависимостей
Установите необходимые библиотеки и системные зависимости для браузеров Playwright:
```
pip install --upgrade pip
pip install -r requirements.txt
pip install pytest-playwright
playwright install chromium
```

### 3. Запуск всех тестов с выводом детальной информации
```
pytest -v
```
### Логирование
Обращения к API и ответы фиксируются в лог-файлах в папке /logs
