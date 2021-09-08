from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Класс c атрибутами - селекторами для поиска на веб-страницах элементов аутентификации пользователя."""

    LOGIN = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "loginbtn")
    FORM = (By.ID, "page-wrapper")
    USER_BUTTON = (By.CLASS_NAME, "userbutton")
    USER_MENU = (By.CLASS_NAME, "usermenu")
    EXIT = (By.ID, "actionmenuaction-6")
    EXIT_CONFIRM = (By.XPATH, "//button[text()='Выход']")
    LOGIN_ERROR = (By.ID, "loginerrormessage")
