from pydantic import BaseModel

class Class(BaseModel):
    id: int
    name: str
    description: str
    id_teacher: int
    id_students: list[int]