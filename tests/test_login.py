import pytest
import time
from pages.main_page import MainPage


class TestLogin:
    """Тесты для страницы логина"""

    @pytest.mark.positive
    def test_successful_login(self, login_page):
        """Позитивный тест: успешный вход"""
        # Тестовые данные
        username = "standard_user"
        password = "secret_sauce"

        # Выполнение логина
        main_page = MainPage(login_page.driver)
        login_page.login(username, password)

        # Проверки
        assert main_page.is_main_page(), "Не удалось войти в систему"
        assert main_page.get_title() == "Products", "Некорректный заголовок страницы"

        # Скриншот для доказательства
        login_page.take_screenshot("success_login.png")

    @pytest.mark.negative
    @pytest.mark.parametrize("username,password,expected_error", [
        ("", "secret_sauce", "Epic sadface: Username is required"),
        ("standard_user", "", "Epic sadface: Password is required"),
        ("invalid", "secret_sauce", "Epic sadface: Username and password do not match any user in this service"),
        ("standard_user", "wrong", "Epic sadface: Username and password do not match any user in this service"),
    ])
    def test_failed_login(self, login_page, username, password, expected_error):
        """Негативные тесты: неуспешный вход"""
        login_page.login(username, password)

        # Проверка сообщения об ошибке
        assert login_page.is_error_displayed(), "Сообщение об ошибке не отображается"
        error_text = login_page.get_error_message()
        assert expected_error in error_text, f"Неверное сообщение об ошибке: {error_text}"

        # Скриншот ошибки
        login_page.take_screenshot(f"failed_login_{username}_{password}.png")

    @pytest.mark.ui
    def test_login_page_elements(self, login_page):
        """Тест наличия элементов на странице логина"""
        login_page.open()

        # Проверка отображения элементов
        assert login_page.is_login_page(), "Логотип не отображается"
        assert login_page.is_element_present(login_page.USERNAME_INPUT), "Поле username отсутствует"
        assert login_page.is_element_present(login_page.PASSWORD_INPUT), "Поле password отсутствует"
        assert login_page.is_element_present(login_page.LOGIN_BUTTON), "Кнопка Login отсутствует"

    @pytest.mark.logout
    def test_logout_functionality(self, login_page):
        """Тест выхода из системы"""
        # Логин
        main_page = MainPage(login_page.driver)
        login_page.login("standard_user", "secret_sauce")
        assert main_page.is_main_page(), "Не удалось войти в систему"

        # Выход
        login_page = main_page.logout()

        # Проверка, что вернулись на страницу логина
        assert login_page.is_login_page(), "Не вернулись на страницу логина"
        assert login_page.is_element_present(login_page.LOGIN_BUTTON), "Кнопка Login отсутствует после выхода"