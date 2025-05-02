from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    age: int
    guardian_contact: str
    guardian_name: str

