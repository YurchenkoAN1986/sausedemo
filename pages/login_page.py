from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Локаторы элементов
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    LOGO = (By.CLASS_NAME, "login_logo")

    def __init__(self, driver):
        super().__init__(driver, "https://www.saucedemo.com/")

    def is_login_page(self):
        """Проверить, что находимся на странице логина"""
        return self.is_element_present(self.LOGO)

    def enter_username(self, username):
        """Ввести имя пользователя"""
        self.fill_field(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password):
        """Ввести пароль"""
        self.fill_field(self.PASSWORD_INPUT, password)
        return self

    def click_login(self):
        """Нажать кнопку входа"""
        self.click_element(self.LOGIN_BUTTON)
        return self

    def login(self, username, password):
        """Выполнить полный процесс входа"""
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    def get_error_message(self):
        """Получить текст ошибки, если есть"""
        if self.is_element_present(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return None

    def is_error_displayed(self):
        """Проверить, отображается ли сообщение об ошибке"""
        return self.is_element_present(self.ERROR_MESSAGE)