from http import HTTPStatus

import allure
import pytest

from api.taiga.users.public_users_client import public_users_client
from models.auth.auth_models import RefreshTokenResponseModel, UserAuthData
from models.auth.user_registry_models import RegistryResponseModel
from models.errors_models import LoginErrorResponse
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
    def test_user_invalid_login_data(self):
        login_data = UserAuthData(username="test", password="123456")
        response = public_users_client().auth(login_data)

        assert_status_code(HTTPStatus.UNAUTHORIZED, response.status_code)

    @allure.title("Авторизация через username")
    def test_login_username(self, get_user_session):
        response = public_users_client().auth(get_user_session.auth)
        schema = RegistryResponseModel.model_validate_json(response.text)

        assert_status_code(HTTPStatus.OK, response.status_code)
        validate_json_schema(response.json(), schema.model_json_schema())

    @allure.title("Авторизация через email")
    def test_login_email(self, get_user_session):
        request_data = UserAuthData(username=get_user_session.auth.email,
                                    password=get_user_session.auth.password)
        response = public_users_client().auth(request_data)
        schema = RegistryResponseModel.model_validate_json(response.text)

        assert_status_code(HTTPStatus.OK, response.status_code)
        validate_json_schema(response.json(), schema.model_json_schema())

    @allure.title("Авторизация с не валидным значением type")
    def test_invalid_value_type(self, get_user_session):
        login_data = UserAuthData(
            username=get_user_session.auth.username,
            password=get_user_session.auth.password,
            type=""
        )
        response = public_users_client().auth(login_data)
        schema = LoginErrorResponse.model_validate_json(response.text)

        assert_status_code(HTTPStatus.BAD_REQUEST, response.status_code)
        validate_json_schema(response.json(), schema.model_json_schema())

    @allure.title("Обновление действующего токена")
    @pytest.mark.xfail(reason="Ошибка 401: Пользователь не авторизован")
    def test_refresh_token(self, get_user_session):
        response = public_users_client().refresh_token(get_user_session.auth)
        schema = RefreshTokenResponseModel.model_validate_json(response.text)

        assert_status_code(HTTPStatus.OK, response.status_code)
        validate_json_schema(response.json(), schema.model_json_schema())
