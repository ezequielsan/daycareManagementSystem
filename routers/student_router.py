from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from http import HTTPStatus
from typing import List, Optional

from models.Student import Student
from repositories.studentRepository import StudentRepository

student_repo = StudentRepository()

router = APIRouter(prefix="/students", tags=["students"])

@router.get("", response_model=List[Student])
def get_students():
    return student_repo.read_all()

@router.get("/quantidade")
def get_students_count():
    quantidade = student_repo.count()
    return {"quantidade": quantidade}

@router.get("/zip")
def download_students_csv_zip():
    zip_path = student_repo.zip_csv()
    return FileResponse(
        path=zip_path,
        filename="students.zip",
        media_type="application/zip"
    )

@router.get("/filter", response_model=List[Student])
def filter_students(
    name: Optional[str] = None,
    age: Optional[int] = None,
    guardian_name: Optional[str] = None
):
    return student_repo.filter(name=name, age=age, guardian_name=guardian_name)

@router.get("/{student_id}", response_model=Student)
def get_student(student_id: int):
    student = student_repo.get_by_id(student_id)
    if not student:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Student not found")
    return student

@router.post("", response_model=Student, status_code=HTTPStatus.CREATED)
def create_student(student: Student):
    result = student_repo.create(student)
    if not result:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="Student already exists")
    return result

@router.put("/{student_id}", response_model=Student, status_code=HTTPStatus.OK)
def update_student(student_id: int, new_student: Student):
    result = student_repo.update(student_id, new_student)
    if not result:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Student not found")
    return result

@router.delete("/{student_id}", status_code=HTTPStatus.OK)
def delete_student(student_id: int):
    result = student_repo.delete(student_id)
    if not result:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Student not found")
    return {"message": "Student deleted successfully"}