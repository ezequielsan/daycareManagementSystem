from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from http import HTTPStatus
from typing import List, Optional

from models.Teacher import Teacher
from repositories.teacherRepository import TeacherRepository

teacher_repo = TeacherRepository()

router = APIRouter(prefix="/teachers", tags=["teachers"])

@router.get("", response_model=List[Teacher])
def get_teachers():
    return teacher_repo.read_all()

@router.get("/quantidade")
def get_teachers_count():
    quantidade = teacher_repo.count()
    return {"quantidade": quantidade}

@router.get("/zip")
def download_teachers_csv_zip():
    zip_path = teacher_repo.zip_csv()
    return FileResponse(
        path=zip_path,
        filename="teachers.zip",
        media_type="application/zip"
    )

@router.get("/filter", response_model=List[Teacher])
def filter_teachers(
    name: Optional[str] = None,
    email: Optional[str] = None,
    educational_background: Optional[str] = None
):
    return teacher_repo.filter(name=name, email=email, educational_background=educational_background)

@router.get("/{teacher_id}", response_model=Teacher)
def get_teacher(teacher_id: int):
    teacher = teacher_repo.get_by_id(teacher_id)
    if not teacher:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Teacher not found")
    return teacher

@router.post("", response_model=Teacher, status_code=HTTPStatus.CREATED)
def create_teacher(teacher: Teacher):
    result = teacher_repo.create(teacher)
    if not result:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="Teacher already exists")
    return result

@router.put("/{teacher_id}", response_model=Teacher, status_code=HTTPStatus.OK)
def update_teacher(teacher_id: int, new_teacher: Teacher):
    result = teacher_repo.update(teacher_id, new_teacher)
    if not result:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Teacher not found")
    return result

@router.delete("/{teacher_id}", status_code=HTTPStatus.OK)
def delete_teacher(teacher_id: int):
    result = teacher_repo.delete(teacher_id)
    if not result:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Teacher not found")
    return {"message": "Teacher deleted successfully"}