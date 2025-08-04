from httpx import Client

from api.core.event_hooks import log_request_event_hook, log_response_event_hook
from config import settings


def public_builder() -> Client:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками для публичных Api.
    :return: Готовый к использованию объект httpx.Client.
    """
    return Client(
        base_url=settings.http_client.base_url,
        timeout=settings.http_client.timeout,
        verify=False,
        event_hooks={
            "request": [log_request_event_hook],
            "response": [log_response_event_hook]
        }
    )
