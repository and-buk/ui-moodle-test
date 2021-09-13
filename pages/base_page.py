from typing import Any
from typing import List
from typing import Optional

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Класс объекта Page Object с базовыми атрибутами и методами."""

    def __init__(self, app: Any) -> None:
        """Конструктор объекта."""
        self.app = app

    def find_element(self, locator: Any, wait_time: int = 10) -> WebElement:
        """
        Находим в течение wait_time секунд с помощью заданного локатора элемент веб-страницы.
        Результат поиска возвращаем в переменной element.
        """
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return element

    def find_elements(self, locator: Any) -> List[WebElement]:
        """Находим все элементы на веб-странице согласно заданного локатора."""
        return self.app.driver.find_elements(*locator)

    @staticmethod
    def fill_element(element: WebElement, text: Optional[Any]) -> WebElement:
        """Заполняем поле элемента веб-страницы текстом."""
        element.clear()
        if text:
            element.send_keys(text)
            return element

    @staticmethod
    def click_element(element: WebElement) -> None:
        """Активируем элемент веб-страницы "нажатием"."""
        element.click()

    def get_clickable_element(self, locator: Any, wait_time: int = 2) -> WebElement:
        """Активируем элемент веб-страницы "нажатием"."""
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.element_to_be_clickable(locator)
        )
        return element

    @staticmethod
    def select_element(element: WebElement, text=None, value=None) -> None:
        """Активируем элемент веб-страницы "нажатием"."""
        if text:
            Select(element).select_by_visible_text(text)
        elif value:
            Select(element).select_by_value(value)

    @staticmethod
    def element_is_visible(element: WebElement):
        return element.is_displayed()
