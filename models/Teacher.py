from pydantic import BaseModel

class Teacher(BaseModel):
    id: int
    name: str
    email:str
    phone: str
    educational_background: str