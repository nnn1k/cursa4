from modules.database.db_class import db
from modules.models.User import User

def create_user_object(res):
    if not res['error'] and res['result']:
        return User(*res['result'][0])
    else:
        return None

def auth_user(login, password) -> User:
    res = db.execute_query('select * from users where login = ? and password = ?', login, password, is_select=True)
    return create_user_object(res)

def add_user(login, password) -> User:
    db.execute_query('insert into users (login, password) values (?, ?)', login, password)
    return get_user_for_login(login)

def get_user_for_login(login) -> User:
    res = db.execute_query('select * from users where login = ?', login, is_select=True)
    return create_user_object(res)

def get_user_for_id(user_id) -> User:
    res = db.execute_query('select * from users where id = ?', user_id,  is_select=True)
    return create_user_object(res)

def get_user_for_email(email) -> User:
    res = db.execute_query('select * from users where email = ?', email,  is_select=True)
    return create_user_object(res)

def filling_form(user_id, name, surname, email, phone, photo_url) -> User:
    db.execute_query('''
        update users 
        set name = ?, surname = ?, email = ?, phone = ?, photo_url = ?
        where id = ?
        ''', name, surname, email, phone, photo_url, user_id)
    return get_user_for_id(user_id)

def update_password(user_id, password) -> User:
    db.execute_query('update users set password = ? where id = ?', password, user_id)
    return get_user_for_id(user_id)

