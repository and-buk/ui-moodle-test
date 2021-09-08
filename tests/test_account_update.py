import pytest

from models.user import UserData


class TestUserData:
    def test_valid_edit_user_data(self, app, auth):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing user data
        5. Edit userl data with valid data
        6. Check successfully editing
        """
        app.user_data.go_to_editing_user_data()
        data = UserData.random()
        app.user_data.user_data_edit(data)
        assert app.user_data.is_changed(), "User data change failed!"

    @pytest.mark.parametrize("field", ["first_name", "last_name", "email"])
    def test_invalid_edit_user_data(self, app, auth, field):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing user data
        5. Edit user data with invalid data
        6. Check editing is not successfully
        """
        app.user_data.go_to_editing_user_data()
        data = UserData.random()
        setattr(data, field, None)
        app.user_data.user_data_edit(data)
        assert (
            not app.user_data.all_required_fields_filled()
        ), "Empty fields are ignored and user data changed successfully!"

    @pytest.mark.parametrize("email", ["3444.com", "fake@.org", "123@123"])
    def test_edit_user_data_with_invalid_email(self, app, auth, email):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing user data
        5. Edit user data with incorrect email
        6. Check editing is not successfully
        """
        app.user_data.go_to_editing_user_data()
        data = UserData(first_name="Дмитрий", last_name="Кошечкин", email=email)
        app.user_data.user_data_edit(data)
        assert (
            not app.user_data.is_email_valid()
        ), "Invalid email accepted and user data changed successfully!"
