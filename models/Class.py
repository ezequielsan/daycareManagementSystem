from typing import List

from models.Base import BaseEntity
from models.Student import Student
from models.Teacher import Teacher


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
