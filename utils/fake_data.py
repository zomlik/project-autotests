from mimesis import Locale, Person


class FakeData:
    """
     Класс для генерации случайных тестовых данных.
    """
    def __init__(self):
        self._person = Person(Locale.EN)

    def username(self) -> str:
        """Генерирует рандомной username"""
        return self._person.username()

    def full_name(self) -> str:
        return self._person.full_name()

    def email(self) -> str:
        return self._person.email()

    def password(self) -> str:
        return self._person.password()


fake = FakeData()
