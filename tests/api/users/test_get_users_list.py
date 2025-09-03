from http import HTTPStatus

import allure
import pytest

from api.taiga.users.private_user_client import private_users_client
from models.errors_models import ErrorMessageModel
from models.user_models import ListUserResponseModel, UserResponseIdModel
from utils.allure_constants import Feature
from utils.asserts import assert_status_code, validate_json_schema


@allure.feature(Feature.USER)
@pytest.mark.api
@pytest.mark.users
class TestGetUsers:
    @allure.title("Получить список всех пользователей без фильтра")
    @pytest.mark.smoke
    def test_get_list_users(self, get_user_session):
        response = private_users_client(get_user_session.auth).get_list_users()
        schema = ListUserResponseModel.model_validate_json(response.text)

        assert_status_code(HTTPStatus.OK, response.status_code)
        validate_json_schema(response.json(), schema.model_json_schema())

    @allure.title("Получить пользователя по id")
    @pytest.mark.smoke
    def test_get_user_by_id(self, get_user_session):
        response = (private_users_client(get_user_session.auth).
                    get_user_by_id(get_user_session.response.id))
        schema = UserResponseIdModel.model_validate_json(response.text)

        assert_status_code(HTTPStatus.OK, response.status_code)
        validate_json_schema(response.json(), schema.model_json_schema())

    @allure.title("Получить пользователя с не валидным id")
    @pytest.mark.regression
    def test_get_user_by_invalid_id(self, get_user_session):
        response = private_users_client(get_user_session.auth).get_user_by_id(0)
        schema = ErrorMessageModel.model_validate_json(response.text)

        assert_status_code(HTTPStatus.NOT_FOUND, response.status_code)
        validate_json_schema(response.json(), schema.model_json_schema())
