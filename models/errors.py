from pydantic import BaseModel


class LoginErrorResponse(BaseModel):
    """Описание структуры ответа на не корректные запросы к Login"""
    _error_message: str
    _error_type: str
