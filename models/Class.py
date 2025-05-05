from models.Base import BaseEntity

class Class(BaseEntity):
    name: str
    description: str
    id_teacher: int
    id_students: list[int]