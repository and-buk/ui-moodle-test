from selenium.webdriver.common.by import By


class CoursePageLocators:
    # Общее
    FULL_COURSE_NAME = (By.ID, "id_fullname")
    SHORT_COURSE_NAME = (By.ID, "id_shortname")
    END_DAY = (By.ID, "id_enddate_day")
    END_MONTH = (By.ID, "id_enddate_month")
    END_YEAR = (By.ID, "id_enddate_year")
    END_HOUR = (By.ID, "id_enddate_hour")
    END_MINUTE = (By.ID, "id_enddate_minute")
    COURSE_ID = (By.ID, "id_idnumber")
    COURSE_DESCRIPTION = (By.ID, "id_summary_editoreditable")
    # Формат курса
    COURSE_FORMAT = (By.XPATH, "//a[text()='Формат курса']")
    SECTION_NUMBER = (By.ID, "id_numsections")
    # Внешний вид
    COURSE_APPEARANCE = (By.XPATH, "//a[text()='Внешний вид']")
    COURSE_LANGUAGE = (By.ID, "id_lang")
    GRADE_DISPLAY_OPTION = (By.ID, "id_showgrades")
    # Файлы и загрузки
    FILES_AND_DOWNLOADS = (By.XPATH, "//a[text()='Файлы и загрузки']")
    MAX_FILE_SIZE = (By.ID, "id_maxbytes")
    # Переименование ролей
    ROLE_RENAME_MENU = (By.XPATH, "//a[text()='Переименование ролей']")
    COURSE_CREATOR_NAME = (By.ID, "id_role_2")
    COURSE_TEACHER_NAME = (By.ID, "id_role_3")
    COURSE_STUDENT_NAME = (By.ID, "id_role_5")
    SAVE_AND_RETURN_BUTTON = (By.ID, "id_saveandreturn")
    EMPTY_FULL_NAME_ERROR = (By.ID, "id_error_fullname")
    EMPTY_SHORT_NAME_ERROR = (By.ID, "id_error_shortname")


class ManageCoursePageLocators:
    COURSES_LIST_DATA = (By.CLASS_NAME, "coursename")
    CREATE_COURSE_BUTTON = (By.XPATH, "//a[text()='Создать новый курс']")
    DELETE_COURSE_BUTTON = (By.XPATH, "//a[text()='Удалить']")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[text()='Удалить']")
    COURSE_DELETE_CONFIRMATION = (By.TAG_NAME, "h2")
    CONTINUE_BUTTON = (By.XPATH, "//button[text()='Продолжить']")

    @staticmethod
    def get_course_locator(course_name):
        return By.XPATH, f"//a[text()='{course_name}']"
