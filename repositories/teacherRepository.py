from models.Teacher import Teacher
from repositories.baseRepository import BaseRepository

class TeacherRepository(BaseRepository[Teacher]):
    def __init__(self):
        super().__init__("data/teachers.csv", Teacher)
    
    def _create_dummy_instance(self) -> Teacher:
        return Teacher(id=0, name="", subject="", email="")

    def filter(self, name: str = None, email: str = None, educational_background: str = None) -> list[Teacher]:
        teachers = self.read_all()
        result = []
        for teacher in teachers:
            if name and name.lower() not in teacher.name.lower():
                continue
            if email and email.lower() not in teacher.email.lower():
                continue
            if educational_background and educational_background.lower() not in teacher.educational_background.lower():
                continue
            result.append(teacher)
        return result