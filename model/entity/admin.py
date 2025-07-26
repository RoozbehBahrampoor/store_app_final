from model.tools.validation import name_validator


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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        name_validator(value)
        self._name = value

    def __repr__(self):
        return f"{self.__dict__}"


def admin():
    return None