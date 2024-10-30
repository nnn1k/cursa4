from modules.database.db_class import db
from modules.models.Subscriptions import Subscriptions
from modules.func.utils import *
from modules.models.Service import Service
from modules.models.Rooms import Rooms

def get_subscriptions(user_id) -> Subscriptions:
    res = db.execute_query('select * from subscriptions where user_id = ?', user_id)

def select_all_services() -> list[Service]:
    res = db.execute_query('select * from services', is_select=True)['result']
    services = []
    for service in res:
        services.append(create_cls_object(service, Service))
    return services

def select_one_services(id) -> Service:
    res = db.execute_query('select * from services where id = ?', id, is_select=True)['result']
    if res:
        return create_cls_object(res[0], Service)
    return None

def select_rooms_for_one_service(id) -> list[Rooms]:
    res = db.execute_query('''select * from rooms where service_id = ?''', id, is_select=True)['result']
    rooms = []
    for room in res:
        rooms.append(create_cls_object(room, Rooms))
    return rooms

def add_sport_activities(user_id: int, service_id: int, room_id: int, date, time):
    coach_id = db.execute_query('select id from coaches where service_id = ? and room_id = ?', service_id, room_id, is_select=True)['result'][0][0]
    print(coach_id)
    price = select_one_services(service_id).price
    db.execute_query('''
    insert into sports_activities (user_id, service_id, coach_id, room_id, date, time, price) values 
    (?, ?, ?, ?, ?, ?, ?)''', user_id, service_id, coach_id, room_id, date, time, price)


