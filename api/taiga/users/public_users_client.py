from httpx import Response

from api.api_client import ApiClient
from api.public_builder import public_builder
from models.auth.auth_model import AuthNormalRequestModel
from utils.routes import ApiRoutes


class PublicUsersClient(ApiClient):
    def auth(self, user_data: AuthNormalRequestModel) -> Response:
        return self.post(ApiRoutes.AUTH, json=user_data.model_dump(by_alias=True))


def public_users_client() -> PublicUsersClient:
    return PublicUsersClient(client=public_builder())
