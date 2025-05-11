from models.Base import BaseEntity
from models.Teacher import Teacher
from models.Student import Student
from typing import List

class Class(BaseEntity):
    name: str
    description: str
    id_teacher: int
    id_students: list[int]

class ClassExpanded(BaseEntity):
    name: str
    description: str
    teacher: Teacher
    students: List[Student]