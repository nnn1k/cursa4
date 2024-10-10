from datetime import datetime

from flask_login import UserMixin

class User(UserMixin):
    id: int
    login: str
    password: str
    name: str
    surname: str
    phone_number: str
    email: str
    balance: int
    photo_url: str
    create_at: datetime
    update_at: datetime

    def __init__(self, id, login, password, name, surname, phone_number, email, balance, photo_url, create_at, update_at):
        self.id = id
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email
        self.balance = balance
        self.photo_url = photo_url
        self.create_at = create_at
        self.update_at = update_at


