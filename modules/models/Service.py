class Service:
    id: int
    name: str
    description: str
    photo_url: str
    price: int
    type_service: str

    def __init__(self, id: int, name: str, description: str, photo_url: str, price: int, service_type: str):
        self.id = id
        self.name = name
        self.description = description
        self.photo_url = photo_url
        self.price = price
        self.type_service = service_type
