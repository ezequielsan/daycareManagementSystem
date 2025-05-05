from models.Base import BaseEntity

class Class(BaseModel):
    name: str
    description: str
    id_teacher: int
    id_students: list[int]