from pydantic import BaseModel, RootModel


class CreateWebhooksRequestModel(BaseModel):
    """Модель описывает создание Webhooks"""
    project: int
    name: str
    url: str
    key: str


class WebhooksResponseModel(BaseModel):
    """Модель описывает структуру ответа для Webhooks"""
    id: int
    key: str
    logs_counter: int
    name: str
    project: int
    url: str


class ListWebhooksResponseModel(RootModel):
    root: list[WebhooksResponseModel]
