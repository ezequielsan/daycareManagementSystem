from typing import List
from repositories.baseRepository import read_data_csv, write_data_csv
from models.Teacher import Teacher
import os
from repositories.baseRepository import BaseRepository

class TeacherRepository(BaseRepository[Teacher]):
    def __init__(self):
        super().__init__("data/teachers.csv", Teacher)
    
    def _create_dummy_instance(self) -> Teacher:
        return Teacher(id=0, name="", subject="", email="")
