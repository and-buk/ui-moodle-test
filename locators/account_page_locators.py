from selenium.webdriver.common.by import By


class AccountPageLocators:
    USER_MENU_SETTINGS = (By.ID, "actionmenuaction-5")
    EDIT_USER_INFO = (By.CSS_SELECTOR, "a[href*='editadvanced']")
    FIRST_NAME_INPUT = (By.ID, "id_firstname")
    LAST_NAME_INPUT = (By.ID, "id_lastname")
    EMAIL_INPUT = (By.ID, "id_email")
    SHOW_USER_EMAIL = (By.ID, "id_maildisplay")
    MOODLE_INPUT = (By.ID, "id_moodlenetprofile")
    CITY_INPUT = (By.ID, "id_city")
    COUNTRY_SELECT = (By.ID, "id_country")
    TIMEZONE_SELECT = (By.ID, "id_timezone")
    ABOUT_USER = (By.ID, "id_description_editoreditable")
    NAME_DETAIL_BUTTON = (By.XPATH, "//*[text()='Дополнительная информация об имени']")
    FIRST_NAME_PHONETIC_INPUT = (By.ID, "id_firstnamephonetic")
    LAST_NAME_PHONETIC_INPUT = (By.ID, "id_lastnamephonetic")
    PATRONYMIC_INPUT = (By.ID, "id_middlename")
    ALTERNATIVE_NAME_INPUT = (By.ID, "id_alternatename")
    USER_INTERESTS_MENU = (By.XPATH, "//*[text()='Интересы']")
    USER_INTERESTS_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Введите теги..."]')
    OPTIONAL_DATA_BUTTON = (By.XPATH, "//*[text()='Необязательное']")
    USER_ID_INPUT = (By.ID, "id_idnumber")
    USER_WORKPLACE_INPUT = (By.ID, "id_institution")
    DEPARTMENT_INPUT = (By.ID, "id_department")
    WORK_PHONE_INPUT = (By.ID, "id_phone1")
    MOBILE_PHONE_INPUT = (By.ID, "id_phone2")
    WORKPLACE_ADDRESS = (By.ID, "id_address")
    UPDATE_ACCOUNT_BUTTON = (By.ID, "id_submitbutton")
    CHANGE_SUCCESSFUL_INFO = (By.CLASS_NAME, "alert-success")
    EMPTY_FIRSTNAME_ERROR = (By.ID, "id_error_firstname")
    EMPTY_LASTTNAME_ERROR = (By.ID, "id_error_lastname")
    EMPTY_EMAIL_ERROR = (By.ID, "id_error_email")
