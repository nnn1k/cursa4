import datetime

class SportsActivities:
    id: int
    user_id: int
    service_id: int
    coach_id: int
    room_id: int
    date: datetime.date
    time: datetime.time
    price: int

    def __init__(self, id, user_id, service_id, coach_id, room_id, date, time, price):
        self.id = id
        self.user_id = user_id
        self.service_id = service_id
        self.coach_id = coach_id
        self.room_id = room_id
        self.date = date
        self.time = time
        self.price = price
