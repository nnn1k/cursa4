from modules.database.db_class import db
from modules.models.Subscriptions import Subscriptions
from modules.func.utils import *
from modules.models.Service import Service

def get_subscriptions(user_id) -> Subscriptions:
    res = db.execute_query('select * from subscriptions where user_id = ?', user_id)

def select_all_services():
    res = db.execute_query('select * from services', is_select=True)['result']
    services = []
    for service in res:
        print(service)
        services.append(create_cls_object(service, Service))
    return services

