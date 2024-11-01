from modules.models.Review import Review
from modules.database.db_class import db
from modules.func.utils import *


def get_reviews():
    res = db.execute_query('''
    select r.id, r.title, r.description, u.id as user_id, u.name, u.surname, r.create_at
    from reviews as r
    inner join users as u 
    on u.id = r.user_id''', is_select=True)['result']
    reviews = []
    for review in res:
        reviews.append(create_cls_object(review, Review))
    return reviews

def add_review(title, description, user_id):
    db.execute_query('insert into reviews (title, description, user_id) values (?, ?, ?)', title, description, user_id)

def get_review_for_user_id(user_id):
    res = db.execute_query(''' 
    select r.id, r.title, r.description, u.id as user_id, u.name, u.surname, r.create_at
    from reviews as r
    inner join users as u 
    on u.id = r.user_id where user_id = ?''', user_id, is_select=True)['result']
    if res:
        return create_cls_object(res[0], Review)
    else:
        return None

def update_review_for_user_id(title, description, user_id):
    db.execute_query('''
    update reviews
    set title = ?, description = ?
    where user_id = ?''', title, description, user_id)

def delete_review_for_user_id(user_id):
    db.execute_query('''delete from reviews where user_id = ?''', user_id)
