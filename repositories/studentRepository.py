from models.Student import Student
from repositories.baseRepository import BaseRepository

class StudentRepository(BaseRepository[Student]):
    def __init__(self):
        super().__init__("data/students.csv", Student)
    
    def _create_dummy_instance(self) -> Student:
        return Student(id=0, name="", age=0, guardian_contact="", guardian_name="")

    def filter(self, name: str = None, age: int = None, guardian_name: str = None) -> list[Student]:
        students = self.read_all()
        result = []
        for student in students:
            if name and name.lower() not in student.name.lower():
                continue
            if age and student.age != age:
                continue
            if guardian_name and guardian_name.lower() not in student.guardian_name.lower():
                continue
            result.append(student)
        return result