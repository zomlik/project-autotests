from pydantic import BaseModel, RootModel


class UserResponseIdModel(BaseModel):
    """Описание структуры ответа на запрос пользователя по ID"""
    id: int
    username: str
    full_name: str
    full_name_display: str
    color: str
    bio: str
    lang: str
    theme: str
    timezone: str
    is_active: bool
    photo: str | None
    big_photo: str | None
    gravatar_id: str
    roles: list[str]
    total_private_projects: int
    total_public_projects: int
    email: str
    uuid: str
    date_joined: str
    read_new_terms: bool
    accepted_terms: bool
    max_private_projects: int | None
    max_public_projects: int | None
    max_memberships_private_projects: int | None
    max_memberships_public_projects: int | None
    verified_email: bool


class UserResponseModel(BaseModel):
    """Описание структуры ответа для списка пользователей"""
    id: int
    username: str
    full_name: str
    full_name_display: str
    color: str
    bio: str
    lang: str
    theme: str
    timezone: str
    is_active: bool
    photo: str | None
    big_photo: str | None
    gravatar_id: str
    roles: list


class ListUserResponseModel(RootModel):
    """Описание структуры ответа на запрос списка пользователей"""
    root: list[UserResponseModel]


class ContactResponseModel(BaseModel):
    comment: str
    created_date: str
    id: int
    project: int
    user: int


class UpdateUserRequestModel(BaseModel):
    username: str


class ChangePasswordRequestModel(BaseModel):
    current_password: str
    password: str


class ChangePasswordRecoveryModel(BaseModel):
    password: str
    token: str
