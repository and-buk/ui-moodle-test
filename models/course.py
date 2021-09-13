from __future__ import annotations

import random
from typing import Any

from faker import Faker

from common.constants import CourseConstants

fake = Faker("Ru-ru")


class CourseData:
    """Класс для представления объекта с данными, необходимыми для создания курса."""

    def __init__(
        self,
        full_course_name: Any = None,
        short_course_name: Any = None,
        end_day: Any = None,
        end_month: Any = None,
        end_year: Any = None,
        end_hour: Any = None,
        end_minute: Any = None,
        course_id: Any = None,
        course_description: Any = None,
        section_number: Any = None,
        course_language: Any = None,
        grade_display_option: Any = None,
        max_file_size: Any = None,
        creator_name: Any = None,
        teacher_name: Any = None,
        student_name: Any = None,
    ):
        """Конструктор объекта."""
        self.full_course_name = full_course_name
        self.short_course_name = short_course_name
        self.end_day = end_day
        self.end_month = end_month
        self.end_year = end_year
        self.end_hour = end_hour
        self.end_minute = end_minute
        self.course_id = course_id
        self.course_description = course_description
        self.section_number = section_number
        self.course_language = course_language
        self.grade_display_option = grade_display_option
        self.max_file_size = max_file_size
        self.creator_name = creator_name
        self.teacher_name = teacher_name
        self.student_name = student_name

    @staticmethod
    def random() -> CourseData:
        """Генерируем случайные данные для заполнения полей."""
        full_course_name = fake.job()
        short_course_name = fake.word()
        end_day = str(random.randint(1, 31))
        end_month = str(random.randint(1, 12))
        end_year = str(random.randint(2022, 2025))
        end_hour = str(random.randint(0, 23))
        end_minute = str(random.randint(0, 59))
        course_id = str(random.randint(0, 100))
        course_description = fake.text(max_nb_chars=200)
        section_number = str(random.randint(4, 10))
        course_language = random.choice(CourseConstants.COURSE_LANGUAGE)
        grade_display_option = random.choice(
            list(CourseConstants.GRADE_OPTIONS.values())
        )
        max_file_size = str(random.choice(CourseConstants.FILE_SIZES_VALUES))
        creator_name = fake.word()
        teacher_name = fake.word()
        student_name = fake.word()
        return CourseData(
            full_course_name,
            short_course_name,
            end_day,
            end_month,
            end_year,
            end_hour,
            end_minute,
            course_id,
            course_description,
            section_number,
            course_language,
            grade_display_option,
            max_file_size,
            creator_name,
            teacher_name,
            student_name,
        )
