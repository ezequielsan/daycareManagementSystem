import csv
from http import HTTPStatus

from fastapi import HTTPException

from models.Class import Class
from repositories.baseRepository import BaseRepository


class ClassRepository(BaseRepository[Class]):
    def __init__(self, teacher_repo, student_repo):
        super().__init__('data/classes.csv', Class)
        self.teacher_repo = teacher_repo
        self.student_repo = student_repo

    def _create_dummy_instance(self) -> Class:
        return Class(
            id=0, name='', description='', id_teacher=0, id_students=[]
        )

    def filter(
        self, name: str = None, id_teacher: int = None, id_student: int = None
    ) -> list[Class]:
        classes = self.read_all()
        result = []
        for classroom in classes:
            if name and name.lower() not in classroom.name.lower():
                continue
            if id_teacher and classroom.id_teacher != id_teacher:
                continue
            if id_student and id_student not in classroom.id_students:
                continue
            result.append(classroom)
        return result

    def expand(self, classroom: Class):
        teacher = self.teacher_repo.get_by_id(classroom.id_teacher)
        students = [
            self.student_repo.get_by_id(sid) for sid in classroom.id_students
        ]
        students = [s for s in students if s is not None]
        return {
            'id': classroom.id,
            'name': classroom.name,
            'description': classroom.description,
            'teacher': teacher,
            'students': students,
        }

    def expand_all(self, classes: list[Class]):
        return [self.expand(c) for c in classes]

    def validate_entities(self, classroom: Class):
        teacher = self.teacher_repo.get_by_id(classroom.id_teacher)
        if not teacher:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail=f'Teacher with id {classroom.id_teacher} not found',
            )
        for sid in classroom.id_students:
            student = self.student_repo.get_by_id(sid)
            if not student:
                raise HTTPException(
                    status_code=HTTPStatus.NOT_FOUND,
                    detail=f'Student with id {sid} not found',
                )

    def write_all(self, data: list[Class]) -> None:
        fieldnames = ['id', 'name', 'description', 'id_teacher', 'id_students']
        with open(self.csv_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for item in data:
                row = item.dict()

                row['id_students'] = '-'.join(
                    str(sid) for sid in row['id_students']
                )
                writer.writerow(row)

    def read_all(self) -> list[Class]:
        classes = []
        try:
            with open(self.csv_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row['id'] = int(row['id'])
                    row['id_teacher'] = int(row['id_teacher'])
                    if row['id_students'].strip() == '':
                        row['id_students'] = []
                    else:
                        row['id_students'] = [
                            int(sid)
                            for sid in row['id_students'].split('-')
                            if sid.strip()
                        ]
                    classes.append(self.model_class(**row))
        except FileNotFoundError:
            return []
        return classes
