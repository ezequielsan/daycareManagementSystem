from models.Classroom import Classroom
from repositories.baseRepository import BaseRepository

class ClassroomRepository(BaseRepository[Classroom]):
    def __init__(self):
        super().__init__("data/classrooms.csv", Classroom)
    
    def _create_dummy_instance(self) -> Classroom:
        return Classroom(id=0, name="", capacity=0, location="")
        
    def filter(self, name: str = None, id_teacher: int = None) -> list[Classroom]:
        classrooms = self.read_all()
        result = []
        for classroom in classrooms:
            if name and name.lower() not in classroom.name.lower():
                continue
            if id_teacher and classroom.id_teacher != id_teacher:
                continue
            result.append(classroom)
        return result