# conftest.py - ПОЛНАЯ ВЕРСИЯ
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os


# Фикстура для драйвера
@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания драйвера"""

    # Путь к драйверу в папке проекта
    current_dir = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(current_dir, "drivers", "chromedriver.exe")

    # Если файла нет - покажем ошибку
    if not os.path.exists(driver_path):
        raise FileNotFoundError(
            f"ChromeDriver не найден: {driver_path}\n"
            "Скачать можно тут: https://googlechromelabs.github.io/chrome-for-testing/"
        )

    # Настройки браузера
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Создаем сервис с явным путем
    service = Service(executable_path=driver_path)

    # Создаем драйвер
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver

    # Закрываем драйвер
    if driver:
        driver.quit()


# Фикстура для страницы логина
@pytest.fixture
def login_page(driver):
    """Фикстура для страницы логина"""
    from pages.login_page import LoginPage
    return LoginPage(driver)


# # Фикстура для главной страницы (если понадобится)
# @pytest.fixture
# def main_page(driver):
#     """Фикстура для главной страницы"""
#     from pages.main_page import MainPage
#     return MainPage(driver)