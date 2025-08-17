from http import HTTPStatus

import pytest
from pydantic import BaseModel

from api.taiga.users.public_users_client import public_users_client
from config import settings
from models.auth.auth_models import UserAuthData
from models.auth.user_registry_models import (
    PublicRegistryRequestModel,
    RegistryResponseModel,
)
from utils.asserts import assert_status_code


class UserFixture(BaseModel):
    request: PublicRegistryRequestModel
    response: RegistryResponseModel
    auth: UserAuthData


def create_new_random_user() -> UserFixture:
    """
    Функция создает случайного пользователя
    :return: Модель UserFixture с данными пользователя
    :raise: Ошибка AssertionError, если статус код ответа не соответствует HTTPStatus.CREATED (201)
    """
    request_data = PublicRegistryRequestModel()

    response = public_users_client().create_public_user(request_data)
    assert_status_code(response.status_code, HTTPStatus.CREATED)

    user_data = UserAuthData(
        username=request_data.username,
        email=request_data.email,
        password=request_data.password
    )

    return UserFixture(request=request_data,
                       response=response.json(),
                       auth=user_data)


@pytest.fixture(scope="session")
def get_user_session() -> UserFixture:
    """
    Фикстура pytest для создания пользователя с областью видимости 'session'.
    Пользователь будет создан один раз на всю тестовую сессию.
    :return: Модель UserFixture с данными для авторизации
    """
    response = create_new_random_user()

    return response


@pytest.fixture(scope="function")
def get_new_user() -> UserFixture:
    """
    Фикстура pytest для создания пользователя с областью видимости 'function'.
    Новый пользователь будет создаваться для каждого теста.
    :return: Модель UserFixture с данными для авторизации
    """
    response = create_new_random_user()

    return response


@pytest.fixture()
def get_super_user() -> UserAuthData:
    """
    Фикстура pytest возвращающая данные для входа с ролью Admin
    :return: Модель UserAuthData с данными для авторизации
    """
    auth_data = UserAuthData(
        email=settings.super_user.email,
        username=settings.super_user.username,
        password=settings.super_user.password)
    return auth_data
