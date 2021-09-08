from __future__ import annotations

import random

from faker import Faker

from common.constants import UserDataConstants

fake = Faker("Ru-ru")


class UserData:
    def __init__(
        self,
        first_name=None,
        last_name=None,
        email=None,
        email_show_config=None,
        moodle_net_profile=None,
        city=None,
        country=None,
        time_zone=None,
        about_user=None,
        image_url="https://image.freepik.com/free-photo/moment-precious-enjoyment-share-inspire_53876-120675.jpg",
        image_description=None,
        first_name_phonetic=None,
        last_name_phonetic=None,
        patronymic=None,
        alternative_name=None,
        interests=None,
        identification_number=None,
        workplace=None,
        department=None,
        work_phone=None,
        mobile_phone=None,
        workplace_address=None,
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.email_show_config = email_show_config
        self.moodle_net_profile = moodle_net_profile
        self.city = city
        self.country = country
        self.time_zone = time_zone
        self.about_user = about_user
        self.image_url = image_url
        self.image_description = image_description
        self.first_name_phonetic = first_name_phonetic
        self.patronymic = patronymic
        self.last_name_phonetic = last_name_phonetic
        self.alternative_name = alternative_name
        self.interests = interests
        self.identification_number = identification_number
        self.workplace = workplace
        self.department = department
        self.work_phone = work_phone
        self.mobile_phone = mobile_phone
        self.workplace_address = workplace_address

    @staticmethod
    def random() -> UserData:
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
        email = fake.email()
        email_show_config = random.choice(
            list(UserDataConstants.EMAIL_SHOW_MODES.values())
        )
        moodle_net_profile = fake.url()
        city = fake.city()
        country = fake.country_code(representation="alpha-2")
        time_zone = random.choice(UserDataConstants.TIMEZONE)
        about_user = fake.text(max_nb_chars=120)
        image_url = "https://image.freepik.com/free-photo/moment-precious-enjoyment-share-inspire_53876-120675.jpg"
        image_description = fake.text(max_nb_chars=15)
        first_name_phonetic = first_name
        patronymic = fake.middle_name_male()
        last_name_phonetic = last_name
        alternative_name_phonetic = fake.text(max_nb_chars=5)
        interests = fake.word()
        identification_number = fake.individuals_inn()
        workplace = fake.company()
        department = fake.job()
        work_phone = fake.phone_number()
        mobile_phone = fake.phone_number()
        workplace_address = fake.address()
        return UserData(
            first_name,
            last_name,
            email,
            email_show_config,
            moodle_net_profile,
            city,
            country,
            time_zone,
            about_user,
            image_url,
            image_description,
            first_name_phonetic,
            last_name_phonetic,
            patronymic,
            alternative_name_phonetic,
            interests,
            identification_number,
            workplace,
            department,
            work_phone,
            mobile_phone,
            workplace_address,
        )
