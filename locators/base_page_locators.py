from selenium.webdriver.common.by import By


class BasePageLocators:
    LOG_IN_TEXT = (By.LINK_TEXT, "Вход")
    HEADER_USER_INFO = (By.XPATH, './/span[@class = "usertext mr-1"]')
