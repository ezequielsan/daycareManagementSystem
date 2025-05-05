from models.Teacher import Teacher
from repositories.baseRepository import BaseRepository

class TeacherRepository(BaseRepository[Teacher]):
    def __init__(self):
        super().__init__("data/teachers.csv", Teacher)
    
    def _create_dummy_instance(self) -> Teacher:
        return Teacher(id=0, name="", subject="", email="")