from os import name
from tkinter.font import names
from typing import re


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
        if not re.match("^[a-zA-Z]{3,30}$", value):
        else:
            self._name = value
        else:
        raise ValueError("Invalid name !!!")

    def __repr__(self):
        return f"{self.__dict__}"
