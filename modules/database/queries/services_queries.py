from modules.database.db_class import db
from modules.models.Subscriptions import Subscriptions
from modules.func.utils import *
from modules.models.Service import Service
from modules.models.Rooms import Rooms
from modules.models.SportsActivitiesHistory import SportsActivitiesHistory
from modules.models.SubscriptionsTypes import SubscriptionsTypes
from modules.models.SubscriptionsHistory import SubscriptionsHistory


def select_all_services() -> list[Service]:
    res = db.execute_query('select * from services', is_select=True)['result']
    services = []
    for service in res:
        services.append(create_cls_object(service, Service))
    return services

def select_one_services(id: int) -> Service:
    res = db.execute_query('select * from services where id = ?', id, is_select=True)['result']
    if res:
        return create_cls_object(res[0], Service)
    return None

def select_rooms_for_one_service(id: int) -> list[Rooms]:
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

def get_sport_activities(user_id: int) -> list[SportsActivitiesHistory]:
    res = db.execute_query('''select sa.id, s.name, sa.date, s.price, s.photo_url 
    from sports_activities as sa 
    inner join services as s
    on s.id = sa.service_id
    where sa.user_id = ?''', user_id, is_select=True)['result']
    s_a = []
    for sa in res:
        s_a.append(create_cls_object(sa, SportsActivitiesHistory))
    return s_a

def get_subscriptions_types() -> list[SubscriptionsTypes]:
    res = db.execute_query('select * from subscriptions_types', is_select=True)['result']
    subscriptions_types = []
    for subscription in res:
        subscriptions_types.append(create_cls_object(subscription, SubscriptionsTypes))
    return subscriptions_types

def get_one_subscriptions_types(subscription_id: int) -> SubscriptionsTypes:
    res = db.execute_query('select * from subscriptions_types where id = ?', subscription_id, is_select=True)['result']
    return create_cls_object(res[0], SubscriptionsTypes)

def add_subscriptions(user_id: int, service_id: int, subscription_type_id: int, date_start, date_end):
    db.execute_query(''' 
    insert into subscriptions (user_id, service_id, subscription_type_id, date_start, date_end) values 
    (?, ?, ?, ?, ?)''', user_id, service_id, subscription_type_id, date_start, date_end)


def get_subscriptions_history(user_id) -> list[SubscriptionsHistory]:
    res = db.execute_query('''select sub.id, s.name, sub.date_start, sub.date_end, sub_t.price, s.photo_url 
                           from subscriptions_types as sub_t 
                           inner join subscriptions as sub
                           on sub_t.id = sub.subscription_type_id
                           inner join services as s 
                           on sub.service_id = s.id
                           where user_id = ?''', user_id, is_select=True)['result']
    subscriptions = []
    for subscription in res:
        subscriptions.append(create_cls_object(subscription, SubscriptionsHistory))
    return subscriptions
