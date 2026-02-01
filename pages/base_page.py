from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.url)
        return self

    def find_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
        return wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, timeout=None):
        """Найти все элементы с ожиданием"""
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
        return wait.until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator, timeout=None):
        """Кликнуть по элементу"""
        element = self.find_element(locator, timeout)
        element.click()
        return element

    def fill_field(self, locator, text, timeout=None):
        """Заполнить поле текстом"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
        return element

    def get_text(self, locator, timeout=None):
        """Получить текст элемента"""
        element = self.find_element(locator, timeout)
        return element.text

    def is_element_present(self, locator, timeout=5):
        """Проверить наличие элемента"""
        try:
            self.find_element(locator, timeout)
            return True
        except TimeoutException:
            return False

    def take_screenshot(self, filename):
        """Сделать скриншот"""
        self.driver.save_screenshot(filename)
        return self