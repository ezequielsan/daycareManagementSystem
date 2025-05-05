from models.Base import BaseEntity

class Classroom(BaseEntity):
    name: str
    capacity: int
    location: str
