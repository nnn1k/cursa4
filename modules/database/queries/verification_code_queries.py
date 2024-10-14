from modules.database.db_class import db
from modules.models.Verification_code import VerificationCode
def add_verification_code(user_id, code):
    db.execute_query('insert into verification_code (user_id, code) values (?, ?)', user_id, code)

    return get_verification_code(code)

def get_verification_code(code) -> VerificationCode:
    res = db.execute_query('select * from verification_code where code = ?', code, is_select=True)['result']
    if res:
        verification_code = VerificationCode(*res[0])
        return verification_code
    else:
        return None

def drop_verification_code(user_id) -> VerificationCode:
    db.execute_query('delete from verification_code where user_id= ?', user_id)


