import datetime

class SubscriptionsHistory:
    id: int
    service_name: str
    date_start: datetime.date
    date_end: datetime.date
    price: int
    service_photo_url: str
    is_active: bool

    def __init__(self, id, name, date_start, date_end, price, service_photo_url, is_active=False):
        self.id = id
        self.name = name
        self.date_start = date_start
        self.date_end = date_end
        self.price = price
        self.service_photo_url = service_photo_url

