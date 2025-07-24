from http import HTTPStatus

import allure

from api.taiga.users.public_users_client import public_users_client
from models.auth.user_registry import PublicRegistryRequestModel, RegistryResponseModel
from utils.allure_constants import Epic, Feature, Tag
from utils.asserts import assert_status_code, validate_json_schema


@allure.epic(Epic.USERS)
@allure.feature(Feature.AUTH)
@allure.tag(Tag.API)
class TestRegistry:
    @allure.title("Регистрация пользователя с валидными данными")
    @allure.testcase("ID-100")
    def test_create_new_user(self):
        user_data = PublicRegistryRequestModel()

        response = public_users_client().create_public_user(user_data)
        schema = RegistryResponseModel.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        validate_json_schema(response.json(), schema.model_json_schema())
