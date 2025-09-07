class RegisterPageLocators:
    USERNAME_FIELD = "//input[@name='username']"
    FULL_NAME_FIELD = "//input[@name='full_name']"
    EMAIL_FIELD = "//input[@name='email']"
    PASSWORD_FIELD = "//input[@name='password']"

    SING_UP_BUTTON = "//button[@title='Sign up']"
    LOGIN_IN_LINK = "//a[@title='Log in']"

    USERNAME_FIELD_ERROR = "#checksley-error-field-2 li"
    PASSWORD_FIELD_ERROR = "#checksley-error-field-5 li"
