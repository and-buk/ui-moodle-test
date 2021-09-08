from selenium.webdriver.common.by import By


class BasePageLocators:
    """
    Класс для работы со значениями базовых элементов веб-страниц,
    изменение которых не предполагается во время тестирования.
    """

    LOG_IN_TEXT = (By.LINK_TEXT, "Вход")
    HEADER_USER_INFO = (By.XPATH, './/span[@class = "usertext mr-1"]')
