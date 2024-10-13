from datetime import datetime

from flask_login import UserMixin

class User(UserMixin):
    id: int
    login: str
    password: str
    name: str
    surname: str
    phone: str
    email: str
    balance: int
    photo_url: str
    create_at: datetime
    update_at: datetime

    def __init__(self, id, login, password, name=None, surname=None, phone=None, email=None, balance=None, photo_url=None, create_at=None, update_at=None):
        self.id = id
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.balance = balance
        self.photo_url = photo_url
        self.create_at = create_at
        self.update_at = update_at


