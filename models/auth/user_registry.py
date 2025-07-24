from pydantic import BaseModel, Field

from utils.fake_data import fake


class PublicRegistryRequestModel(BaseModel):
    """Описание структуры запроса для публичной регистрации"""
    accepted_terms: str = Field(default="true")
    email: str = Field(default_factory=fake.email)
    full_name: str = Field(default_factory=fake.full_name)
    password: str = Field(default_factory=fake.password)
    type: str = Field(default="public")
    username: str = Field(default_factory=fake.username)


class RegistryResponseModel(BaseModel):
    """Описание структуры ответа для регистрации"""
    accepted_terms: bool
    big_photo: str | None
    bio: str
    color: str
    date_joined: str
    email: str
    full_name: str
    full_name_display: str
    gravatar_id: str
    id: int
    is_active: bool
    lang: str
    max_memberships_private_projects: int | None
    max_memberships_public_projects: int | None
    max_private_projects: int | None
    max_public_projects: int | None
    photo: str | None
    read_new_terms: bool
    roles: list
    theme: str
    timezone: str
    total_private_projects: int
    total_public_projects: int
    username: str
    uuid: str
