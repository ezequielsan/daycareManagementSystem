from http import HTTPStatus
from typing import List
from fastapi import FastAPI, HTTPException
<<<<<<< HEAD
from repositories.baseRepository import read_data_csv, write_data_csv
from repositories.teacherRepository import TeacherRepository
=======

>>>>>>> 636e236534e3141a02cd3ebf552d3b450b02d43c
from models.Teacher import Teacher
from models.Student import Student
from repositories.teacherRepository import TeacherRepository
from repositories.studentRepository import StudentRepository

app = FastAPI()

<<<<<<< HEAD
teacher_repository = TeacherRepository()
=======
teacher_repo = TeacherRepository()
student_repo = StudentRepository()
>>>>>>> 636e236534e3141a02cd3ebf552d3b450b02d43c

@app.get("/")
def read_root():
    return {"Hello": "World"}

# CRUD Teacher
@app.get("/teachers", response_model=List[Teacher])
def get_teachers():
<<<<<<< HEAD
    return teacher_repository.get_all_teachers()
=======
    return teacher_repo.read_all()
>>>>>>> 636e236534e3141a02cd3ebf552d3b450b02d43c

@app.get("/teachers/{teacher_id}", response_model=Teacher)
def get_teacher(teacher_id: int):
    teacher = teacher_repo.get_by_id(teacher_id)
    if not teacher:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Teacher not found")
    return teacher

@app.post("/teachers", response_model=Teacher, status_code=HTTPStatus.CREATED)
def create_teacher(teacher: Teacher):
    result = teacher_repo.create(teacher)
    if not result:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="Teacher already exists")
    return result

@app.put("/teachers/{teacher_id}", response_model=Teacher, status_code=HTTPStatus.OK)
def update_teacher(teacher_id: int, new_teacher: Teacher):
    result = teacher_repo.update(teacher_id, new_teacher)
    if not result:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Teacher not found")
    return result

@app.delete("/teachers/{teacher_id}", status_code=HTTPStatus.OK)
def delete_teacher(teacher_id: int):
    result = teacher_repo.delete(teacher_id)
    if not result:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Teacher not found")
    return {"message": "Teacher deleted successfully"}

# CRUD Student
@app.get("/students", response_model=List[Student])
def get_students():
    return student_repo.read_all()

@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    student = student_repo.get_by_id(student_id)
    if not student:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Student not found")
    return student

@app.post("/students", response_model=Student, status_code=HTTPStatus.CREATED)
def create_student(student: Student):
    result = student_repo.create(student)
    if not result:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="Student already exists")
    return result

@app.put("/students/{student_id}", response_model=Student, status_code=HTTPStatus.OK)
def update_student(student_id: int, new_student: Student):
    result = student_repo.update(student_id, new_student)
    if not result:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Student not found")
    return result

@app.delete("/students/{student_id}", status_code=HTTPStatus.OK)
def delete_student(student_id: int):
    result = student_repo.delete(student_id)
    if not result:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Student not found")
    return {"message": "Student deleted successfully"}