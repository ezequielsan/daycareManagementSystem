from models.Base import BaseEntity

class Student(BaseEntity):
    name: str
    age: int
    guardian_contact: str
    guardian_name: str

