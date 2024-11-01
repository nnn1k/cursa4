import datetime


class Review:
    id: int
    title: str
    description: str
    user_id: int
    user_name: str
    user_surname: str
    create_at: datetime

    def __init__(self, id, title, description, user_id, user_name, user_surname, create_at):
        self.id = id
        self.title = title
        self.description = description
        self.user_id = user_id
        self.user_name = user_name
        self.user_surname = user_surname
        self.create_at = create_at
