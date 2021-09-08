from selenium.webdriver.remote.webelement import WebElement

from common.constants import UserDataConstants
from locators.account_page_locators import AccountPageLocators
from locators.login_page_locators import LoginPageLocators
from models.user import UserData
from pages.base_page import BasePage


class AccountPage(BasePage):
    def user_menu(self) -> WebElement:
        return self.find_element(LoginPageLocators.USER_MENU)

    def user_menu_settings(self) -> WebElement:
        return self.find_element(AccountPageLocators.USER_MENU_SETTINGS)

    def go_to_editing_user_data(self) -> None:
        self.click_element(self.user_menu())
        self.click_element(self.user_menu_settings())
        self.click_element(self.find_element(AccountPageLocators.EDIT_USER_INFO))

    def first_name_input(self) -> WebElement:
        return self.find_element(AccountPageLocators.FIRST_NAME_INPUT)

    def last_name_input(self) -> WebElement:
        return self.find_element(AccountPageLocators.LAST_NAME_INPUT)

    def email_input(self) -> WebElement:
        return self.find_element(AccountPageLocators.EMAIL_INPUT)

    def email_show_config(self) -> WebElement:
        return self.find_element(AccountPageLocators.SHOW_USER_EMAIL)

    def moodle_profile_input(self) -> WebElement:
        return self.find_element(AccountPageLocators.MOODLE_INPUT)

    def city_input(self) -> WebElement:
        return self.find_element(AccountPageLocators.CITY_INPUT)

    def country_select(self) -> WebElement:
        return self.find_element(AccountPageLocators.COUNTRY_SELECT)

    def time_zone_select(self) -> WebElement:
        return self.find_element(AccountPageLocators.TIMEZONE_SELECT)

    def about_user_input(self) -> WebElement:
        return self.find_element(AccountPageLocators.ABOUT_USER)

    def add_image_button(self) -> WebElement:
        return self.find_element(AccountPageLocators.ADD_IMAGE)

    def upload_by_url(self) -> WebElement:
        return self.find_element(AccountPageLocators.UPLOAD_BY_URL)

    def image_url_input(self) -> WebElement:
        return self.find_element(AccountPageLocators.IMAGE_URL_INPUT)

    def upload_image_button(self) -> WebElement:
        return self.find_element(AccountPageLocators.UPLOAD_IMAGE_BUTTON)

    def image_select(self) -> WebElement:
        return self.find_element(AccountPageLocators.IMAGE_ICON)

    def confirm_file(self) -> WebElement:
        return self.find_element(AccountPageLocators.CONFIRM_FILE)

    def image_description_input(self) -> WebElement:
        return self.find_element(AccountPageLocators.IMAGE_DESCRIPTION)

    def additional_name_button(self) -> WebElement:
        return self.find_element(AccountPageLocators.NAME_DETAIL_BUTTON)

    def firstname_phonetic_input(self) -> WebElement:
        return self.find_element(AccountPageLocators.FIRST_NAME_PHONETIC_INPUT)

    def lastname_phonetic_input(self) -> WebElement:
        return self.find_element(AccountPageLocators.LAST_NAME_PHONETIC_INPUT)

    def middle_name_input(self) -> WebElement:
        return self.find_element(AccountPageLocators.PATRONYMIC_INPUT)

    def alternative_name_input(self) -> WebElement:
        return self.find_element(AccountPageLocators.ALTERNATIVE_NAME_INPUT)

    def user_interests_menu(self) -> WebElement:
        return self.find_element(AccountPageLocators.USER_INTERESTS_MENU)

    def interests_input(self) -> WebElement:
        return self.find_element(AccountPageLocators.USER_INTERESTS_INPUT)

    def optional_data_menu(self) -> WebElement:
        return self.find_element(AccountPageLocators.OPTIONAL_DATA_BUTTON)

    def id_input(self) -> WebElement:
        return self.find_element(AccountPageLocators.USER_ID_INPUT)

    def workpalce_input(self) -> WebElement:
        return self.find_element(AccountPageLocators.USER_WORKPLACE_INPUT)

    def department_input(self) -> WebElement:
        return self.find_element(AccountPageLocators.DEPARTMENT_INPUT)

    def work_phone_input(self) -> WebElement:
        return self.find_element(AccountPageLocators.WORK_PHONE_INPUT)

    def mobile_phone_input(self) -> WebElement:
        return self.find_element(AccountPageLocators.MOBILE_PHONE_INPUT)

    def address_input(self) -> WebElement:
        return self.find_element(AccountPageLocators.WORKPLACE_ADDRESS)

    def submit_changes(self) -> WebElement:
        return self.find_element(AccountPageLocators.UPDATE_ACCOUNT_BUTTON)

    def user_data_edit(self, data: UserData) -> None:
        self.fill_element(self.first_name_input(), data.first_name)
        self.fill_element(self.last_name_input(), data.last_name)
        self.fill_element(self.email_input(), data.email)
        self.select_element(self.email_show_config(), text=data.email_show_config)
        self.fill_element(self.moodle_profile_input(), data.moodle_net_profile)
        self.fill_element(self.city_input(), data.city)
        self.select_element(self.country_select(), value=data.country)
        self.select_element(self.time_zone_select(), value=data.time_zone)
        self.fill_element(self.about_user_input(), data.about_user)
        self.fill_element(self.image_description_input(), data.image_description)
        self.click_element(self.additional_name_button())
        self.fill_element(self.firstname_phonetic_input(), data.first_name_phonetic)
        self.fill_element(self.lastname_phonetic_input(), data.last_name_phonetic)
        self.fill_element(self.middle_name_input(), data.patronymic)
        self.fill_element(self.alternative_name_input(), data.alternative_name)
        self.click_element(self.user_interests_menu())
        self.fill_element(self.interests_input(), data.interests)
        self.click_element(self.optional_data_menu())
        self.fill_element(self.id_input(), data.identification_number)
        self.fill_element(self.workpalce_input(), data.workplace)
        self.fill_element(self.department_input(), data.department)
        self.fill_element(self.work_phone_input(), data.work_phone)
        self.fill_element(self.mobile_phone_input(), data.mobile_phone)
        self.fill_element(self.address_input(), data.workplace_address)
        self.click_element(self.submit_changes())

    def is_changed(self) -> bool:
        element = self.find_element(AccountPageLocators.CHANGE_SUCCESSFUL_INFO).text
        if UserDataConstants.USER_DATA_CHANGE_MESSAGE in element:
            return True
        return False

    def all_required_fields_filled(self) -> bool:
        empty_first_name_field_error = self.find_element(
            AccountPageLocators.EMPTY_FIRSTNAME_ERROR
        ).text
        empty_last_name_field_error = self.find_element(
            AccountPageLocators.EMPTY_LASTTNAME_ERROR
        ).text
        empty_email_field_error = self.find_element(
            AccountPageLocators.EMPTY_EMAIL_ERROR
        ).text

        if (
            UserDataConstants.EMPTY_NAME_FIELD_MESSAGE in empty_first_name_field_error
            or UserDataConstants.EMPTY_NAME_FIELD_MESSAGE in empty_last_name_field_error
            or UserDataConstants.EMPTY_EMAIL_FIELD_MESSAGE in empty_email_field_error
        ):
            return False
        return True

    def is_email_valid(self) -> bool:
        element = self.find_element(AccountPageLocators.EMPTY_EMAIL_ERROR).text
        if UserDataConstants.INVALID_EMAIL_MESSAGE in element:
            return False
        return True
