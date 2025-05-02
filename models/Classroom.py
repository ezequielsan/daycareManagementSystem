from pydantic import BaseModel


class Classroom(BaseModel):
    id: int
    name: str
    capacity: int
    location: str
