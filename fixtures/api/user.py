from http import HTTPStatus

import pytest

from api.taiga.users.public_users_client import public_users_client
from models.auth.user_registry import PublicRegistryRequestModel
from utils.asserts import assert_status_code


@pytest.fixture()
def create_new_user() -> PublicRegistryRequestModel:
    """
    Фикстура создает, нового пользователя
    :return: Возвращает, модель PublicRegistryRequestModel с данными для авторизации
    """
    data = PublicRegistryRequestModel()

    response = public_users_client().create_public_user(data)
    assert_status_code(response.status_code, HTTPStatus.CREATED)

    return data
