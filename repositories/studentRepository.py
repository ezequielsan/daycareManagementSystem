from models.Student import Student
from repositories.baseRepository import BaseRepository

class StudentRepository(BaseRepository[Student]):
    def __init__(self):
        super().__init__("data/students.csv", Student)
    
    def _create_dummy_instance(self) -> Student:
        return Student(id=0, name="", age=0, guardian_contact="", guardian_name="")