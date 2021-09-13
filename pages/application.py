from typing import Any

from pages.account_page import AccountPage
from pages.course_page import CoursePage
from pages.login_page import LoginPage


class Application:
    """Класс для представления объекта, позволяющего с помощью определённого драйвера взаимодействовать с браузером."""

    def __init__(self, driver: Any, url: str) -> None:
        """Конструктор объекта."""
        self.driver = driver
        self.url = url
        self.login = LoginPage(self)
        self.user_data = AccountPage(self)
        self.course = CoursePage(self)

    def open_main_page(self) -> None:
        """Открываем в браузере веб-страницу по заданному адресу."""
        self.driver.get(self.url)

    def quit(self) -> None:
        """Закрываем браузер."""
        self.driver.quit()

    def open_auth_page(self) -> None:
        """Открываем в браузере веб-страницу аутентификации пользователя."""
        self.driver.get(self.url + "/login/index.php")
