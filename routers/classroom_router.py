from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from http import HTTPStatus
from typing import List, Optional

from models.Classroom import Classroom
from repositories.classroomRepository import ClassroomRepository

classroom_repo = ClassroomRepository()

router = APIRouter(prefix="/classrooms", tags=["classrooms"])

@router.get("", response_model=List[Classroom])
def get_classrooms():
    return classroom_repo.read_all()

@router.get("/quantidade")
def get_classrooms_count():
    quantidade = classroom_repo.count()
    return {"quantidade": quantidade}

@router.get("/zip")
def download_classrooms_csv_zip():
    zip_path = classroom_repo.zip_csv()
    return FileResponse(
        path=zip_path,
        filename="classrooms.zip",
        media_type="application/zip"
    )

@router.get("/filter", response_model=List[Classroom])
def filter_classrooms(
    name: Optional[str] = None,
    id_teacher: Optional[int] = None
):
    return classroom_repo.filter(name=name, id_teacher=id_teacher)

@router.get("/{classroom_id}", response_model=Classroom)
def get_classroom(classroom_id: int):
    classroom = classroom_repo.get_by_id(classroom_id)
    if not classroom:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Classroom not found")
    return classroom

@router.post("", response_model=Classroom, status_code=HTTPStatus.CREATED)
def create_classroom(classroom: Classroom):
    result = classroom_repo.create(classroom)
    if not result:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="Classroom already exists")
    return result

@router.put("/{classroom_id}", response_model=Classroom, status_code=HTTPStatus.OK)
def update_classroom(classroom_id: int, new_classroom: Classroom):
    result = classroom_repo.update(classroom_id, new_classroom)
    if not result:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Classroom not found")
    return result

@router.delete("/{classroom_id}", status_code=HTTPStatus.OK)
def delete_classroom(classroom_id: int):
    result = classroom_repo.delete(classroom_id)
    if not result:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Classroom not found")
    return {"message": "Classroom deleted successfully"}