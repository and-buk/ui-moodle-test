from __future__ import annotations

from typing import Any

from faker import Faker

fake = Faker("Ru-ru")


class AuthData:
    """Класс для представления объекта с данными, необходимыми для аутентификации пользователя."""

    def __init__(self, login: Any = None, password: Any = None):
        """Конструктор объекта."""
        self.login = login
        self.password = password

    @staticmethod
    def random() -> AuthData:
        """Генерируем случайные данные для аутентификации пользователя."""
        login = fake.email()
        password = fake.password()
        return AuthData(login, password)
