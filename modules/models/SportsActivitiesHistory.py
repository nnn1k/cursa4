import datetime


class SportsActivitiesHistory:
    id: int
    service_name: str
    date: datetime.date
    price: int
    service_photo_url: str

    def __init__(self, id, service_name, date, price, service_photo_url):
        self.id = id
        self.service_name = service_name
        self.date = date
        self.price = price
        self.service_photo_url = service_photo_url
