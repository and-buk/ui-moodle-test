from selenium.webdriver.remote.webelement import WebElement

import conftest
from locators.course_page_locators import CoursePageLocators
from locators.course_page_locators import ManageCoursePageLocators
from locators.login_page_locators import LoginPageLocators
from models.course import CourseData
from pages.base_page import BasePage


class CoursePage(BasePage):
    def sidebar_button(self) -> WebElement:
        return self.find_element(LoginPageLocators.SIDEBAR_BUTTON)

    def is_sidebar_open(self) -> bool:
        element = self.find_element(LoginPageLocators.SIDEBAR_MENU)
        is_open = self.element_is_visible(element)
        if is_open:
            return True
        return False

    def administration_button(self) -> WebElement:
        return self.get_clickable_element(LoginPageLocators.ADMINISTRATION_BUTTON)

    def courses_button(self) -> WebElement:
        return self.find_element(LoginPageLocators.COURSES_HEADER)

    def manage_courses_button(self) -> WebElement:
        return self.find_element(LoginPageLocators.MANAGE_COURSES_BUTTON)

    def create_course_button(self) -> WebElement:
        return self.find_element(ManageCoursePageLocators.CREATE_COURSE_BUTTON)

    def is_course_exist(self, data: CourseData) -> bool:
        elements = self.find_elements(ManageCoursePageLocators.COURSES_LIST_DATA)
        courses_list = [c.text for c in elements]
        if data.full_course_name in courses_list:
            return True
        return False

    def go_to_design_courses_frame(self) -> None:
        if not self.is_sidebar_open():
            self.click_element(self.sidebar_button())
        self.click_element(self.administration_button())
        self.click_element(self.courses_button())
        self.click_element(self.manage_courses_button())
        self.click_element(self.create_course_button())

    def full_course_name_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.FULL_COURSE_NAME)

    def short_course_name_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.SHORT_COURSE_NAME)

    def course_end_day_select(self) -> WebElement:
        return self.find_element(CoursePageLocators.END_DAY)

    def course_end_month_select(self) -> WebElement:
        return self.find_element(CoursePageLocators.END_MONTH)

    def course_end_year_select(self) -> WebElement:
        return self.find_element(CoursePageLocators.END_YEAR)

    def course_end_hour_select(self) -> WebElement:
        return self.find_element(CoursePageLocators.END_HOUR)

    def course_end_minute_select(self) -> WebElement:
        return self.find_element(CoursePageLocators.END_MINUTE)

    def course_id_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.COURSE_ID)

    def course_description_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.COURSE_DESCRIPTION)

    def course_format_button(self) -> WebElement:
        return self.find_element(CoursePageLocators.COURSE_FORMAT)

    def course_section_number_select(self) -> WebElement:
        return self.find_element(CoursePageLocators.SECTION_NUMBER)

    def course_appearance_button(self) -> WebElement:
        return self.find_element(CoursePageLocators.COURSE_APPEARANCE)

    def course_language_select(self) -> WebElement:
        return self.find_element(CoursePageLocators.COURSE_LANGUAGE)

    def grade_display_select(self) -> WebElement:
        return self.find_element(CoursePageLocators.GRADE_DISPLAY_OPTION)

    def files_and_downloads_button(self) -> WebElement:
        return self.find_element(CoursePageLocators.FILES_AND_DOWNLOADS)

    def max_file_size_select(self) -> WebElement:
        return self.find_element(CoursePageLocators.MAX_FILE_SIZE)

    def role_rename_button(self) -> WebElement:
        return self.find_element(CoursePageLocators.ROLE_RENAME_MENU)

    def course_creator_name_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.COURSE_CREATOR_NAME)

    def course_teacher_name_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.COURSE_TEACHER_NAME)

    def course_student_name_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.COURSE_STUDENT_NAME)

    def save_return_button(self) -> WebElement:
        return self.find_element(CoursePageLocators.SAVE_AND_RETURN_BUTTON)

    def chooose_created_course_button(self, course_name):
        return self.find_element(
            ManageCoursePageLocators.get_course_locator(course_name)
        )

    def delete_course_button(self) -> WebElement:
        return self.find_element(ManageCoursePageLocators.DELETE_COURSE_BUTTON)

    def confirm_delete_button(self) -> WebElement:
        return self.find_element(ManageCoursePageLocators.CONFIRM_DELETE_BUTTON)

    def course_delete_confirmation(self) -> WebElement:
        return self.find_element(ManageCoursePageLocators.COURSE_DELETE_CONFIRMATION)

    def continue_button(self) -> WebElement:
        return self.find_element(ManageCoursePageLocators.CONTINUE_BUTTON)

    def full_name_error_message(self) -> WebElement:
        return self.find_element(CoursePageLocators.EMPTY_FULL_NAME_ERROR)

    def short_name_error_message(self) -> WebElement:
        return self.find_element(CoursePageLocators.EMPTY_SHORT_NAME_ERROR)

    def create_course(self, data: CourseData) -> None:
        self.go_to_design_courses_frame()
        self.fill_element(self.full_course_name_input(), data.full_course_name)
        self.fill_element(self.short_course_name_input(), data.short_course_name)
        self.select_element(self.course_end_day_select(), value=data.end_day)
        self.select_element(self.course_end_month_select(), value=data.end_month)
        self.select_element(self.course_end_year_select(), value=data.end_year)
        self.select_element(self.course_end_hour_select(), value=data.end_hour)
        self.select_element(self.course_end_minute_select(), value=data.end_minute)
        self.fill_element(self.course_id_input(), data.course_id)
        self.fill_element(self.course_description_input(), data.course_description)
        self.click_element(self.course_format_button())
        self.select_element(
            self.course_section_number_select(), value=data.section_number
        )
        self.click_element(self.course_appearance_button())
        self.select_element(self.course_language_select(), value=data.course_language)
        self.select_element(self.grade_display_select(), text=data.grade_display_option)
        self.click_element(self.files_and_downloads_button())
        self.select_element(self.max_file_size_select(), value=data.max_file_size)
        self.click_element(self.role_rename_button())
        self.fill_element(self.course_creator_name_input(), data.creator_name)
        self.fill_element(self.course_teacher_name_input(), data.teacher_name)
        self.fill_element(self.course_student_name_input(), data.student_name)
        self.click_element(self.save_return_button())
        conftest.logger.info(f"Создан курс '{data.full_course_name}'")

    def remove_course(self, data: CourseData) -> None:
        conftest.logger.info(f"Курс '{data.full_course_name}' удалён!")
        self.click_element(self.chooose_created_course_button(data.full_course_name))
        self.click_element(self.delete_course_button())
        self.click_element(self.confirm_delete_button())
        self.continue_button()

    def all_required_fields_filled(self) -> bool:
        if self.full_name_error_message() or self.short_name_error_message():
            return False
        return True
