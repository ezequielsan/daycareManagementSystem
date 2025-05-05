from models.Base import BaseEntity

class Teacher(BaseEntity):
    name: str
    email:str
    phone: str
    educational_background: str