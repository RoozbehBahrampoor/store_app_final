from model.tools.admin_validation import name_validator, family_validator, username_validator, email_validator, \
    password_validator, code_validator, locked_validator


class Admin:
    def __init__(self, code, name, family, email, username, password, locked=False):
        self.code = code
        self.name = name
        self.family = family
        self.email = email
        self.username = username
        self.password = password
        self.locked = locked

    @property
    def code(self):
        return self.code

    @code.setter
    def code(self, value):
        code_validator(value)
        self.code = (value)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        name_validator(value)
        self._name = value

    @property
    def family(self):
        return self.family

    @family.setter
    def family(self, value):
        family_validator(value)
        self._family = value

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, value):
        email_validator(value)
        self._validate_email(value)

    @property
    def username(self):
        return self.username

    @username.setter
    def username(self, value):
        username_validator(value)
        self._username = (value)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, value):
        password_validator(value)
        self._password = (value)

    @property
    def locked(self):
        return self.locked

    @locked.setter
    def locked(self, value):
        locked_validator(value)
        self._locked = (value)

    def __repr__(self):
        return f"{self.__dict__}"


def admin():
    return None
