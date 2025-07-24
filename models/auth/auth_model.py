from pydantic import BaseModel, Field


class AuthNormalRequestModel(BaseModel):
    """Описание структуры запроса на нормальную авторизацию"""
    username: str
    type: str = Field(default="normal")
    password: str
