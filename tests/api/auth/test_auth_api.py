from http import HTTPStatus

import allure
import pytest

from api.taiga.users.public_users_client import public_users_client
from models.auth.auth_model import AuthNormalRequestModel
from utils.allure_constants import Epic, Feature
from utils.asserts import assert_status_code


@allure.epic(Epic.USERS)
@allure.feature(Feature.AUTH)
@pytest.mark.api
@pytest.mark.auth
@pytest.mark.users
class TestAuth:

    @allure.title("Авторизация пользователя с не валидными данными")
    @allure.testcase("ID-171")
    def test_user_login(self):
        user_data = AuthNormalRequestModel(username="test", password="123456")
        response = public_users_client().auth(user_data)

        assert_status_code(HTTPStatus.BAD_REQUEST, response.status_code)
