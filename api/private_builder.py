from httpx import Client

from api.event_hooks import log_request_event_hook, log_response_event_hook
from api.taiga.auth_client import auth_client
from config import settings
from models.auth.auth_model import AuthNormalRequestModel


def private_builder(login_data: AuthNormalRequestModel) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками для API
    требующих авторизацию.
    :return: Готовый к использованию объект httpx.Client.
    """
    get_auth_client = auth_client()
    response = get_auth_client.login(AuthNormalRequestModel(
        username=login_data.username,
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
