from http import HTTPStatus

import allure
import pytest

from api.taiga.webhooks.webhooks_client import webhooks_client
from models.webhooks.webhooks_models import ListWebhooksResponseModel
from utils.allure_constants import Feature
from utils.asserts import assert_equal, assert_status_code, validate_json_schema


@allure.feature(Feature.WEBHOOKS)
@pytest.mark.api
@pytest.mark.webhooks
class TestGetWebHooks:

    @allure.title("Получение списка Webhooks")
    @pytest.mark.smoke
    def test_get_list_webhooks(self, get_user_session):
        response = webhooks_client(get_user_session.auth).get_webhooks_list()
        schema = ListWebhooksResponseModel.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), schema.model_json_schema())

    @allure.title("Получение списка Webhooks с не существующим проектом")
    @pytest.mark.regression
    def test_get_list_webhooks_invalid_project(self, get_user_session):
        response = webhooks_client(get_user_session.auth).get_webhooks_list(project=0)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_equal(response.json(), [])
