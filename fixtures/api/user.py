from http import HTTPStatus

import pytest

from api.taiga.users.public_users_client import public_users_client
from config import settings
from models.auth.auth_models import UserAuthData
from models.auth.user_registry_models import PublicRegistryRequestModel
from utils.asserts import assert_status_code


def create_new_random_user() -> UserAuthData:
    """
    Функция создает случайного пользователя
    :return: Модель UserAuthData с данными для авторизации
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

    return user_data


@pytest.fixture(scope="session")
def get_user_session() -> UserAuthData:
    """
    Фикстура pytest для создания пользователя с областью видимости 'session'.
    Пользователь будет создан один раз на всю тестовую сессию.
    :return: Модель UserAuthData с данными для авторизации
    """
    response = create_new_random_user()

    return response


@pytest.fixture(scope="function")
def get_new_user() -> UserAuthData:
    """
    Фикстура pytest для создания пользователя с областью видимости 'function'.
    Новый пользователь будет создаваться для каждого теста.
    :return: Модель UserAuthData с данными для авторизации
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
