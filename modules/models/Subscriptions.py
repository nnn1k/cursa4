import datetime

class Subscriptions:
    id: int
    user_id: int
    service_id: int
    subscription_type_id: int
    date_start: datetime.date
    date_end: datetime.date

    def __init__(self, id, user_id, service_id, subscription_type_id, date_start, date_end):
        self.id = id
        self.user_id = user_id
        self.service_id = service_id
        self.subscription_type_id = subscription_type_id
        self.date_start = date_start
        self.date_end = date_end
