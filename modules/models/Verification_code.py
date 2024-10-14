import datetime

class VerificationCode:
    id: int
    code: str
    user_id: int
    create_at: datetime

    def __init__(self, id=None, user_id=None, code=None, create_at=None):
        self.id = id
        self.user_id = user_id
        self.code = code
        self.create_at = create_at
