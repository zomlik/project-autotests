from pydantic import BaseModel, Field


class AuthNormalRequestModel(BaseModel):
    """Описание структуры запроса на нормальную авторизацию"""
    username: str
    type: str = Field(default="normal")
    password: str


class RefreshTokenRequestModel(BaseModel):
    """Описание структуры запроса на обновление токена"""
    refresh: str


class RefreshTokenResponseModel(BaseModel):
    """Описание структуры ответа запроса на обновление токена"""
    auth_token: str
    refresh: str
