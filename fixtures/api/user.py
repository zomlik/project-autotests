from http import HTTPStatus

import pytest

from api.taiga.users.public_users_client import public_users_client
from models.auth.user_registry import PublicRegistryRequestModel
from utils.asserts import assert_status_code


def create_new_random_user() -> PublicRegistryRequestModel:
    data = PublicRegistryRequestModel()

    response = public_users_client().create_public_user(data)
    assert_status_code(response.status_code, HTTPStatus.CREATED)

    return data


@pytest.fixture(scope="session")
def user_session() -> PublicRegistryRequestModel:
    response = create_new_random_user()

    return response


@pytest.fixture(scope="function")
def new_user() -> PublicRegistryRequestModel:
    response = create_new_random_user()

    return response
