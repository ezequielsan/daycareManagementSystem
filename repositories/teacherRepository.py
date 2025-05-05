<<<<<<< HEAD
from typing import List
from repositories.baseRepository import read_data_csv, write_data_csv
from models.Teacher import Teacher
import os

class TeacherRepository:
    def __init__(self, file_path: str = "data/teachers.csv"):
        self.file_path = file_path

    def get_all_teachers(self) -> List[Teacher]:
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File {self.file_path} not found.")
        return read_data_csv(self.file_path, Teacher)
        

    def get_teacher_by_id(self, teacher_id):
        """
        This method should return a teacher by their ID.
        """
        pass
    def add_teacher(self, teacher):
        """
        This method should add a new teacher to the repository.
        """
        pass
    def update_teacher(self, teacher_id, teacher):
        """
        This method should update an existing teacher in the repository.
        """
        pass        
    def delete_teacher(self, teacher_id):
        """ 
        This method should delete a teacher from the repository.
        """
        pass
    
=======
from models.Teacher import Teacher
from repositories.baseRepository import BaseRepository

class TeacherRepository(BaseRepository[Teacher]):
    def __init__(self):
        super().__init__("data/teachers.csv", Teacher)
    
    def _create_dummy_instance(self) -> Teacher:
        return Teacher(id=0, name="", subject="", email="")
>>>>>>> 636e236534e3141a02cd3ebf552d3b450b02d43c
