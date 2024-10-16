import datetime

class SportsActivities:
    id: int
    user_id: int
    service_id: int
    coach_id: int
    room_id: int
    time_start: datetime
    time_end: datetime
    price: int

    def __init__(self, id, user_id=None, service_id=None, coach_id=None, room_id=None, time_start=None, time_end=None, price=None):
        self.id = id
        self.user_id = user_id
        self.service_id = service_id
        self.coach_id = coach_id
        self.room_id = room_id
        self.time_start = time_start
        self.time_end = time_end
        self.price = price
