class Customer:
    def __init__(self, code, name, family, email, username, password, phone_number,locked=False):
        self.code = code
        self.name = name
        self.family = family
        self.email = email
        self.username = username
        self.password = password
        self.phone = phone_number
        self.locked = locked
        self.address = None


    def __repr__(self):
        return f"{self.__dict__}"
