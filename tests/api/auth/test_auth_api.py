from http import HTTPStatus

import allure
import pytest

from api.taiga.users.public_users_client import public_users_client
from models.auth.auth_model import AuthNormalRequestModel
from models.auth.user_registry import RegistryResponseModel
from models.errors import LoginErrorResponse
from utils.allure_constants import Epic, Feature
from utils.asserts import assert_status_code, validate_json_schema


@allure.epic(Epic.USERS)
@allure.feature(Feature.AUTH)
@pytest.mark.api
@pytest.mark.auth
@pytest.mark.users
class TestAuth:

    @allure.title("Авторизация пользователя с не валидными данными")
    @pytest.mark.regression
    def test_user_valid_login(self):
        login_data = AuthNormalRequestModel(username="test", password="123456")
        response = public_users_client().auth(login_data)

        assert_status_code(HTTPStatus.UNAUTHORIZED, response.status_code)

    @allure.title("Авторизация через username")
    def test_login_username(self, user_session):
        login_data = AuthNormalRequestModel(
            username=user_session.username,
            password=user_session.password)
        response = public_users_client().auth(login_data)
        schema = RegistryResponseModel.model_validate_json(response.text)

        assert_status_code(HTTPStatus.OK, response.status_code)
        validate_json_schema(response.json(), schema.model_json_schema())

    @allure.title("Авторизация через email")
    def test_login_email(self, user_session):
        login_data = AuthNormalRequestModel(
            username=user_session.email,
            password=user_session.password)
        response = public_users_client().auth(login_data)
        schema = RegistryResponseModel.model_validate_json(response.text)

        assert_status_code(HTTPStatus.OK, response.status_code)
        validate_json_schema(response.json(), schema.model_json_schema())

    @allure.title("Авторизация с не валидным значением type")
    def test_invalid_value_type(self, user_session):
        login_data = AuthNormalRequestModel(
            username=user_session.username,
            password=user_session.password,
            type="123"
        )
        response = public_users_client().auth(login_data)
        schema = LoginErrorResponse.model_validate_json(response.text)

        assert_status_code(HTTPStatus.BAD_REQUEST, response.status_code)
        validate_json_schema(response.json(), schema.model_json_schema())
