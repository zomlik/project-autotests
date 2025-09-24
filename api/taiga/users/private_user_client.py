import allure
from httpx import Response

from api.core.api_client import ApiClient
from api.core.private_builder import private_builder
from models.auth.auth_models import UserAuthData
from models.user_models import (
    ChangePasswordRecoveryModel,
    ChangePasswordRequestModel,
    UpdateUserRequestModel,
)
from utils.url import ApiRoutes


class PrivateUsersClient(ApiClient):
    """
        Клиент для работы с /api/v1/users
    """
    @allure.step("Получить список пользователей")
    def get_list_users(self, project: int = None) -> Response:
        """
        Метод выполняет запрос на получение всех пользователей
        :param project: Фильтрация по id проекта
        :return: Объект Response с данными ответа
        """
        return self.get(ApiRoutes.USERS, params={"project": project})

    @allure.step("Получить пользователя по id")
    def get_user_by_id(self, user_id: int) -> Response:
        """
        Метод выполняет запрос на получение конкретного пользователя по id
        :param user_id: id пользователя
        :return: Объект Response с данными ответа
        """
        return self.get(url=f"{ApiRoutes.USERS}/{user_id}")

    @allure.step("Получить данные авторизированного пользователя")
    def get_me(self):
        return self.get(url=f"{ApiRoutes.USERS}/me")

    @allure.step("Получить статистику пользователя")
    def get_user_stats(self, user_id: int) -> Response:
        """
        Метод выполняет запрос на получение статистики пользователя
        :param user_id: id пользователя
        :return: Объект Response с данными ответа
        """
        return self.get(url=f"{ApiRoutes.USERS}/{user_id}//stats")

    @allure.step("Получить статистику по просмотрам пользователя")
    def get_user_watched_content(self, user_id: int,
                                 type_content: str | None = None,
                                 q: str | None = None) -> Response:
        """
        Метод выполняет запрос на получение статистики по просмотрам пользователя
        :param user_id: id пользователя
        :param type_content: Фильтр по типу контента. Например, project, userstory, task and issue
        :param q: Фильтр по названию в теме элемента
        :return: Объект Response с данными ответа
        """
        return self.get(url=f"{ApiRoutes.USERS}/{user_id}/watched", params={"type_content": type_content,
                                                                            "q": q})

    @allure.step("Получение статистики по лайкам пользователя")
    def get_user_liked_content(self, user_id: int, q: str | None = None) -> Response:
        """
        Метод выполняет запрос на получение статистики по лайкам пользователя
        :param user_id: id пользователя
        :param q: Фильтр по названию в теме элемента
        :return: Объект Response с данными ответа
        """
        return self.get(url=f"{ApiRoutes.USERS}/{user_id}/liked")

    @allure.step("Получение статистики по голосованию пользователя")
    def get_user_voted_content(self, user_id: int,
                               type_content: str | None = None,
                               q: str | None = None) -> Response:
        """
        Метод выполняет запрос на получение статистики по голосованию пользователя
        :param user_id: id пользователя
        :param type_content: Фильтр по типу контента. Например, project, userstory, task and issue
        :param q: Фильтр по названию в теме элемента
        :return: Объект Response с данными ответа
        """
        return self.get(url=f"{ApiRoutes.USERS}/{user_id}/voted", params={"type_content": type_content,
                                                                          "q": q})

    def get_user_contact(self, user_id: int, q: str | None = None) -> Response:
        """
        Метод выполняет запрос на получение контактов пользователя
        :param user_id: id пользователя
        :param q: Фильтр по названию в теме элемента
        :return: Объект Response с данными ответа
        """
        return self.get(url=f"{ApiRoutes.USERS}/{user_id}/contacts", params={"q": q})

    def update_user_put(self, payload: UpdateUserRequestModel, user_id: int) -> Response:
        """
        Метод выполняет полное обновление данных пользователя
        :param payload: Модель данных UpdateUserRequestModel
        :param user_id: id пользователя
        :return: Объект Response с данными ответа
        """
        return self.put(url=f"{ApiRoutes.USERS}/{user_id}", json=payload.model_dump(by_alias=True))

    def update_user_path(self, payload, user_id: int) -> Response:
        """
        Метод выполняет частичное обновление данных пользователя
        :param payload:Модель данных UpdateUserRequestModel
        :param user_id: id пользователя
        :return: Объект Response с данными ответа
        """
        return self.patch(url=f"{ApiRoutes.USERS}/{user_id}", json=payload)

    def delete_user(self, user_id: int) -> Response:
        """
        Метод выполняет удаление пользователя по его id
        :param user_id: id пользователя
        :return: Объект Response с данными ответа
        """
        return self.delete(url=f"{ApiRoutes.USERS}/{user_id}")

    def cancel_user_account(self, user_id: int, payload) -> Response:
        """
        Метод блокирует пользователя по id (нужен пользователь с правами admin)
        :param user_id: id пользователя
        :param payload: Данные пользователя
        :return: Объект Response с данными ответа
        """
        return self.post(url=f"{ApiRoutes.USERS}/{user_id}", json=payload)

    def change_user_avatar(self, file) -> Response:
        """
        Метод обновляет аватар пользователя
        :param file: Файл с изображением
        :return: Объект Response с данными ответа
        """
        return self.post(url=f"{ApiRoutes.USERS}/change_avatar")

    def remove_user_avatar(self) -> Response:
        return self.post(url=f"{ApiRoutes.USERS}/remove_avatar")

    def change_user_email(self, email_token: str) -> Response:
        return self.post(url=f"{ApiRoutes.USERS}/change_email", json={"email_token": email_token})

    def change_user_password(self, payload: ChangePasswordRequestModel) -> Response:
        """
        Метод обновления пароля пользователя
        :param payload: Данные для обновления пароля
        :return: Объект Response с данными ответа
        """
        return self.post(url=f"{ApiRoutes.USERS}/change_password",
                         json=payload.model_dump(by_alias=True))

    def recovery_user_password(self, username: str):
        return self.post(url=f"{ApiRoutes.USERS}/password_recovery", json={"username": username})

    def change_user_from_recovery(self, payload: ChangePasswordRecoveryModel) -> Response:
        return self.post(url=f"{ApiRoutes.USERS}/change_password_from_recovery", json=payload)


def private_users_client(auth_data: UserAuthData) -> PrivateUsersClient:
    return PrivateUsersClient(client=private_builder(auth_data))
