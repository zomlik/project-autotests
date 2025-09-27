from http import HTTPStatus

import allure
import pytest

from api.taiga.users.private_user_client import private_users_client
from models.errors_models import ErrorMessageModel
from models.users.user_models import ChangePasswordRequestModel
from utils.allure_constants import Feature
from utils.asserts import assert_equal, assert_status_code, validate_json_schema


@allure.feature(Feature.USERS)
@pytest.mark.api
@pytest.mark.users
class TestUserSettings:

    @allure.title("Изменение пароля пользователя")
    @pytest.mark.smoke
    def test_change_user_password(self, get_new_user):
        payload_data = ChangePasswordRequestModel(
            current_password=get_new_user.request.password,
            password="123456"
        )
        response = private_users_client(get_new_user.auth).change_user_password(payload_data)

        assert_status_code(response.status_code, HTTPStatus.NO_CONTENT)

    @allure.title("Изменение пароля пользователя на пустое значение")
    @pytest.mark.regression
    def test_change_user_empty_password(self, get_user_session):
        payload_data = ChangePasswordRequestModel(
            current_password=get_user_session.request.password,
            password=""
        )
        response = private_users_client(get_user_session.auth).change_user_password(payload_data)
        schema = ErrorMessageModel.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        assert_equal(response.json()["_error_message"], "New password parameter needed")
        validate_json_schema(response.json(), schema.model_json_schema())

    @allure.title("Изменение пароля на пароль длинной менее 6 символов")
    @pytest.mark.regression
    def test_new_password_length(self, get_user_session):
        payload_data = ChangePasswordRequestModel(
            current_password=get_user_session.request.password,
            password="123"
        )
        response = private_users_client(get_user_session.auth).change_user_password(payload_data)
        schema = ErrorMessageModel.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        assert_equal(response.json()["_error_message"],
                     "Invalid password length at least 6 characters needed")
        validate_json_schema(response.json(), schema.model_json_schema())

    @allure.title("Изменение пароля с не валидным текущем паролем")
    @pytest.mark.regression
    def test_change_invalid_current_password(self, get_user_session):
        payload_data = ChangePasswordRequestModel(
            current_password="123",
            password="123456"
        )
        response = private_users_client(get_user_session.auth).change_user_password(payload_data)
        schema = ErrorMessageModel.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        assert_equal(response.json()["_error_message"], "Invalid current password")
        validate_json_schema(response.json(), schema.model_json_schema())

    @allure.title("Отправка запроса на восстановления пароля пользователя")
    @pytest.mark.smoke
    def test_password_recovery(self, get_new_user):
        response = private_users_client(get_new_user.auth).recovery_user_password(
            username=get_new_user.request.username
        )

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_equal(response.json()["detail"], "Mail sent successfully!")
