from http import HTTPStatus

import allure
import pytest

from api.taiga.users.public_users_client import public_users_client
from models.auth.auth_model import AuthNormalRequestModel
from utils.allure import Epic, Feature, Tag


@allure.epic(Epic.USERS)
@allure.feature(Feature.AUTH)
@allure.tag(Tag.API)
@pytest.mark.auth
@pytest.mark.users
class TestAuth:

    @allure.title("Авторизация пользователя с не валидными данными")
    @allure.testcase("ID-171")
    def test_user_login(self):
        get_auth_client = public_users_client()
        response = get_auth_client.auth(
            AuthNormalRequestModel(
                username="test",
                password="123456"
            ))
        assert response.status_code == HTTPStatus.UNAUTHORIZED
