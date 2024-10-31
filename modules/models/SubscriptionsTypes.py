class SubscriptionsTypes:
    id: int
    name: str
    description: str
    time_duration: int
    duration: str
    price: int

    def __init__(self, id, name, description, time_duration, duration, price):
        self.id = id
        self.name = name
        self.description = description
        self.time_duration = time_duration
        self.duration = duration
        self.price = price
