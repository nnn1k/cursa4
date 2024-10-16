import datetime

class Subscriptions:
    id: int
    user_id: int
    service_id: int
    subscription_type_id: int
    date_start: datetime
    date_end: datetime

    def __init__(self, id=None, user_id=None, service_id=None, subscription_type_id=None, date_start=None, date_end=None):
        self.id = id
        self.user_id = user_id
        self.service_id = service_id
        self.subscription_type_id = subscription_type_id
        self.date_start = date_start
        self.date_end = date_end
