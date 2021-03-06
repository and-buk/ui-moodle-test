[![Build Status](https://app.travis-ci.com/and-buk/ui-moodle-test.svg?branch=main)](https://app.travis-ci.com/and-buk/ui-moodle-test)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Тестирование web-приложения [test_moodle_2021](https://qacoursemoodle.innopolis.university/)

## Настройка виртуальной среды и установка программных модулей в OC MS Windows 10

1. Скачайте и установите на локальный компьютер [Python 3.9+](https://www.python.org/)
2. Скачайте все файлы из репозитория на локальный компьютер
3. Установите программный модуль для создания и настройки виртуального окружения
```
pip install virtualenv
```
4. Создайте с помощью командной строки Windows виртуальное окружение **env** для проекта
```
py -m venv env
```
5. Активируйте с помощью командной строки Windows созданное виртуальное окружение
```
env\Scripts\activate
```
6. Установите программные модули из файла requirements.txt. Наберите в командной строке Windows:
```
pip install -r requirements.txt
```
7. Устанавите **Allure**
   1. Скачать [**архив**](https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/) последней версии.
   2. Распаковать в папке на локальном компьютере
   3. Скопировать путь к **bin** папке **Allure**
   4. Добавить местоположение программы, скопированный путь в переменную среды PATH по следующему алгоритму
      1. Нажать кнопку "Пуск"
      2. Нажать кнопку "Параметры"
      3. Выбрать раздел "Система"
      4. Выбрать подраздел "О программе"
      5. Нажать кнопку "Дополнительные параметры системы"
      6. В окне "Свойства системы" нажать кнопку "Параметры среды"
      7. Выбрать переменную среды "Path"
      8. Нажать кнопку "Изменить"
      9. Нажать кнопку "Создать"
      10. Вставить скопированную ссылку на bin папку
   5. Установить [**Java**](https://www.java.com/ru/download/help/windows_manual_download.html)
      1. Скопировать местоположение с Java
      2. Создать новую переменную среды пользователя с наименованием **JAVA_HOME**:
         1. Нажать кнопку "Пуск"
         2. Нажать кнопку "Параметры"
         3. Выбрать раздел "Система"
         4. Выбрать подраздел "О программе"
         5. Нажать кнопку "Дополнительные параметры системы"
         6. В окне "Свойства системы" нажать кнопку "Параметры среды"
         7. Нажать кнопку "Создать"
         8. В поле "Имя" вписать JAVA_HOME
         9. В поле "Значение" вставить путь к Java

## Описание проекта

### Блок проверок на авторизацию пользователя
- авторизация пользователя с валидными логином и паролем (позитивный тест)
- авторизация пользователя с невалидными логином и паролем (негативный тест)
- авторизация пользователя с пустым логином иили паролем (негативный тест)

### Блок проверок на изменение профиля пользователя
- редактирование профиля с валидными данными (позитивный тест)
- редактирование профиля с пустыми полями, обязательными для заполнения (негативный тест)
- редактирование профиля с невалидным адресом электронной почты (негативный тест)

### Блок проверок на создание учебного курса
- создание курса с валидными данными (позитивный тест)
- создание курса с пустыми полями, обязательными для заполнения (негативный тест)

## Запуск проверок

- Без **Allure** отчёта:
  - Всех тестов из папки **tests** командой в командной строке Windows:
    ```
    pytest
    ```
  - Позитивных тестов из папки **tests** командой в командной строке Windows:
    ```
    pytest -m positive
    ```
  - Негативный тестов из папки **tests** командой в командной строке Windows:
    ```
    pytest -m negative
    ```

- C **Allure** отчётом:
  - Генерируем тестовые данные для отчёта командой в командной строке Windows:
    ```
    pytest --alluredir=allure_reports
    ```
  - Создаём и открываем отчёт на странице браузера командой в командной строке Windows:
    ```
    allure serve allure_reports
    ```
