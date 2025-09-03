from pydantic import BaseModel


class LoginErrorResponseModel(BaseModel):
    """Описание структуры ответа на не корректные запросы к Login"""
    _error_message: str
    _error_type: str


class TokenErrorResponseModel(BaseModel):
    """Описание структуры ответа на не корректные запросы к Token"""
    detail: str
    code: str


class ErrorMessageModel(BaseModel):
    """Описание общей структуры для ошибок"""
    _error_message: str
