from http import HTTPStatus
from typing import List, Optional

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from models.Class import Class, ClassExpanded
from repositories.classRepository import ClassRepository
from repositories.studentRepository import StudentRepository
from repositories.teacherRepository import TeacherRepository

teacher_repo = TeacherRepository()
student_repo = StudentRepository()
class_repo = ClassRepository(teacher_repo, student_repo)

router = APIRouter(prefix='/classes', tags=['classes'])


@router.get('', response_model=List[ClassExpanded])
def get_classes():
    classes = class_repo.read_all()
    return class_repo.expand_all(classes)


@router.get('/quantidade')
def get_classes_count():
    quantidade = class_repo.count()
    return {'quantidade': quantidade}


@router.get('/zip')
def download_classes_csv_zip():
    zip_path = class_repo.zip_csv()
    return FileResponse(
        path=zip_path, filename='classes.zip', media_type='application/zip'
    )


@router.get('/filter', response_model=List[ClassExpanded])
def filter_classes(
    name: Optional[str] = None,
    id_teacher: Optional[int] = None,
    id_student: Optional[int] = None,
):
    classes = class_repo.filter(
        name=name, id_teacher=id_teacher, id_student=id_student
    )
    return class_repo.expand_all(classes)


@router.get('/{class_id}', response_model=ClassExpanded)
def get_class(class_id: int):
    classroom = class_repo.get_by_id(class_id)
    if not classroom:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Class not found'
        )
    return class_repo.expand(classroom)


@router.post('', response_model=ClassExpanded, status_code=HTTPStatus.CREATED)
def create_class(classroom: Class):
    class_repo.validate_entities(classroom)
    result = class_repo.create(classroom)
    if not result:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail='Class already exists'
        )
    return class_repo.expand(result)


@router.put(
    '/{class_id}', response_model=ClassExpanded, status_code=HTTPStatus.OK
)
def update_class(class_id: int, new_class: Class):
    class_repo.validate_entities(new_class)
    result = class_repo.update(class_id, new_class)
    if not result:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Class not found'
        )
    return class_repo.expand(result)


@router.delete('/{class_id}', status_code=HTTPStatus.OK)
def delete_class(class_id: int):
    result = class_repo.delete(class_id)
    if not result:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Class not found'
        )
    return {'message': 'Class deleted successfully'}
