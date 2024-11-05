class Rooms:
    id: int
    name: str
    description: str
    length: int
    width: int
    height: int
    photo_url: str
    service_id: int

    def __init__(self, id, name, description, length, width, height, photo_url, service_id):
        self.id = id
        self.name = name
        self.description = description
        self.length = length
        self.width = width
        self.height = height
        self.photo_url = photo_url
        self.service_id = service_id
