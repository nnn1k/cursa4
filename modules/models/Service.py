class Service:
    id: int
    name: str
    description: str
    photo_url: str

    def __init__(self, id: int, name: str, description: str, photo_url: str):
        self.id = id
        self.name = name
        self.description = description
        self.photo_url = photo_url