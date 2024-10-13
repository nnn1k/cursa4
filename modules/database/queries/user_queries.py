from modules.database.db_class import db
from modules.models.User import User

def auth_user(login, password) -> User:
    res = db.execute_query('select * from users where login = ? and password = ?',
                           login, password, is_select=True)
    if not res['error'] and res['result']:
        user = User(*res['result'][0])
        return user
    else:
        return None

def get_user_for_login(login) -> User:
    res = db.execute_query('select * from users where login = ?', login, is_select=True)
    if not res['error'] and res['result']:
        user = User(*res['result'][0])
        return user
    else:
        return None
def add_user(login, password) -> User:
    db.execute_query('insert into users (login, password) values (?, ?)', login, password)

    return get_user_for_login(login)

def get_user_for_id(user_id) -> User:
    res = db.execute_query('select * from users where id = ?', user_id,  is_select=True)['result']

    if res:
        user = User(*res[0])
        return user
    else:
        return None

def filling_form(user_id, name, surname, email, phone) -> User:
    db.execute_query('''
        update users 
        set name = ?, surname = ?, email = ?, phone = ?
        where id = ?
        ''', name, surname, email, phone, user_id)
    print('user update')
    return get_user_for_id(user_id)


