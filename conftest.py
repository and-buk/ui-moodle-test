import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from models.auth import AuthData
from pages.application import Application

logger = logging.getLogger("moodle")


def pytest_addoption(parser):
    """Добавляем опции командной строки."""
    parser.addoption(
        "--base-url",
        action="store",
        default="https://qacoursemoodle.innopolis.university/",
        help="enter base_url",
    ),
    parser.addoption(
        "--username", action="store", default="andrei_inn", help="enter username"
    ),
    parser.addoption(
        "--password", action="store", default="@nDre1_inn", help="enter password"
    )


@pytest.fixture
def auth(app, request) -> None:
    """Аутентификация пользователя."""
    user = request.config.getoption("--username")
    password = request.config.getoption("--password")
    app.open_auth_page()
    data = AuthData(login=user, password=password)
    app.login.auth(data)


@pytest.fixture(scope="session")
def app(request):
    """Адаптер для работы методов объектов PageObject с драйвером браузера."""
    # Инициализируем драйвер для работы с браузером
    base_url = request.config.getoption("--base-url")
    logger.info(f"Start moodle {base_url}")
    chrome_options = Options()
    chrome_options.headless = False
    fixture = Application(
        webdriver.Chrome(
            ChromeDriverManager().install(), chrome_options=chrome_options
        ),
        base_url,
    )
    yield fixture
    # Завершаем работу. Закрываем браузер.
    fixture.quit()


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == "call" and rep.failed:
#         try:
#             if "app" in item.fixturenames:
#                 web_driver = item.funcargs["app"]
#             else:
#                 logger.error("Fail to take screen-shot")
#                 return
#             logger.info('Screen-shot done')
#             allure.attach(
#                 web_driver.driver.get_screenshot_as_png(),
#                 name="screenshot",
#                 attachment_type=allure.attachment_type.PNG,
#             )
#         except Exception as e:
#             logger.error("Fail to take screen-shot: {}".format(e))
