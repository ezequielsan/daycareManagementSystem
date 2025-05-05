from models.Classroom import Classroom
from repositories.baseRepository import BaseRepository

class ClassroomRepository(BaseRepository[Classroom]):
    def __init__(self):
        super().__init__("data/classrooms.csv", Classroom)
    
    def _create_dummy_instance(self) -> Classroom:
        return Classroom(id=0, name="", capacity=0, location="")