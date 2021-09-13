import pytest

from models.course import CourseData


class TestCourseCreate:
    @pytest.mark.positive
    def test_course_creation_with_valid_data(self, app, auth):
        """
        Steps
        1. Open auth page
        2. Auth with an valid data
        3. Go to a course creation page
        4. Create course with valid data
        5. Check that course has been created successfully
        6. Remove the course
        """
        app.course.go_to_design_courses_frame()
        data = CourseData.random()
        app.course.create_course(data)
        assert app.course.is_course_exist(data), "Course creation failed!"
        app.course.remove_course(data)

    @pytest.mark.negative
    @pytest.mark.parametrize("field", ["full_course_name", "short_course_name"])
    def test_course_creation_with_invalid_data(self, app, auth, field):
        """
        Steps
        1. Open auth page
        2. Auth with an valid data
        3. Go to a course creation page
        4. Use invalid data to create a course
        5. Check that course will not be created with invalid data
        """
        app.course.go_to_design_courses_frame()
        data = CourseData.random()
        setattr(data, field, None)
        app.course.create_course(data)
        assert (
            not app.course.all_required_fields_filled()
        ), "Empty fields are ignored and a course created successfully!"
