import re

def code_validator(code):
    if not re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', code):
        raise ValueError("Invalid code")
def name_validator(name):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", name):
        raise ValueError("Invalid name !!!")
def family_validator(family):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", family):
        raise ValueError("Invalid family !!!")
def email_validator(email):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", email):
        raise ValueError("Invalid email !!!")
def username_validator(username):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", username):
        raise ValueError("Invalid username !!!")
def password_validator(password):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", password):
        raise ValueError("Invalid password !!!")
def locked_validator(locked):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", locked):
        raise ValueError("Invalid locked !!!")

