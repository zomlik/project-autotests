class LoginPageLocator:
    """Локаторы для страницы Авторизации"""
    USERNAME_FIELD = "//input[@name='username']"
    PASSWORD_FIELD = "//input[@name='password']"
    LOGIN_BUTTON = "//button[@title='Login']"
    CREATE_ACCOUNT_LINK = "//a[@href='register']"
