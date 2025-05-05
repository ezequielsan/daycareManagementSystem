from http import HTTPStatus
from typing import List
from fastapi import FastAPI, HTTPException
from repositories.baseRepository import read_data_csv, write_data_csv
from repositories.teacherRepository import TeacherRepository
from models.Teacher import Teacher

app = FastAPI()

teacher_repository = TeacherRepository()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# CRUD Teacher
@app.get("/teachers", response_model=List[Teacher])
def get_teachers():
    return teacher_repository.get_all_teachers()

@app.get("/teachers/{teacher_id}", response_model=Teacher)
def get_teacher(teacher_id: int):
    teachers = read_data_csv("data/teachers.csv", Teacher)
    for teacher in teachers:
        if teacher.id == teacher_id:
            return teacher
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Teacher not found")


@app.post("/teachers", response_model=Teacher, status_code=HTTPStatus.CREATED)
def create_teacher(teacher: Teacher):
    teachers = read_data_csv("data/teachers.csv", Teacher)
    if any(teacher.id == t.id for t in teachers):
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="Teacher already exists")
    
    teachers.append(teacher)
    write_data_csv("data/teachers.csv", teachers)
    return teacher

@app.put("/teachers/{teacher_id}", response_model=Teacher, status_code=HTTPStatus.OK)
def update_teacher(teacher_id: int, new_teacher: Teacher):
    teachers = read_data_csv("data/teachers.csv", Teacher)
    for index, teacher in enumerate(teachers):
        if teacher.id == teacher_id:
            if new_teacher != teacher_id:
                new_teacher.id = teacher_id
            teachers[index] = new_teacher
            write_data_csv("data/teachers.csv", teachers)
            return new_teacher
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Teacher not found")

@app.delete("/teachers/{teacher_id}", status_code=HTTPStatus.OK)
def delete_teacher(teacher_id: int):
    teachers = read_data_csv("data/teachers.csv", Teacher)
    filtered_teachers = [teacher for teacher in teachers if teacher.id != teacher_id]

    if (len(teachers) == len(filtered_teachers)):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Teacher not found")
    
    write_data_csv("data/teachers.csv", filtered_teachers)