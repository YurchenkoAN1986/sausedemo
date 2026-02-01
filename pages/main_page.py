from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    # Локаторы
    APP_LOGO = (By.CLASS_NAME, "app_logo")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        # URL главной страницы после логина
        super().__init__(driver, "https://www.saucedemo.com/inventory.html")

    def is_main_page(self):
        """Успешный логин"""
        return self.is_element_present(self.APP_LOGO)

    def get_title(self):
        """Получаем заголовок страницы"""
        return self.get_text(self.PRODUCTS_TITLE)

    def logout(self):
        """Выйти из системы"""
        self.click_element(self.BURGER_MENU)
        self.click_element(self.LOGOUT_LINK)
        # Импорт LoginPage внутри метода
        from pages.login_page import LoginPage
        return LoginPage(self.driver)