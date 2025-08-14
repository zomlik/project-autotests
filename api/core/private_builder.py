from httpx import Client

from api.core.event_hooks import log_request_event_hook, log_response_event_hook
from api.taiga.auth.auth_client import auth_client
from config import settings
from models.auth.auth_models import AuthNormalRequestModel, UserAuthData


def private_builder(login_data: UserAuthData) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками для API
    требующих авторизацию.
    :return: Готовый к использованию объект httpx.Client.
    """
    response = auth_client().login(AuthNormalRequestModel(
        username=login_data.username or login_data.email,
        password=login_data.password
    ))
    return Client(
        base_url=settings.http_client.base_url,
        timeout=settings.http_client.timeout,
        headers={"Authorization": f"Bearer {response.auth_token}"},
        verify=False,
        event_hooks={
            "request": [log_request_event_hook],
            "response": [log_response_event_hook]
        }
    )
