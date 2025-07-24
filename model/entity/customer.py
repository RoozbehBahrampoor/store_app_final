class Customer:
    def __init__(self, code, name, family, email, username, password, locked=False):
        self.code = code
        self.name = name
        self.family = family
        self.email = email
        self.username = username
        self.password = password
        self.locked = locked
        self.address = None


    def __repr__(self):
        return f"{self.__dict__}"
