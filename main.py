from http import HTTPStatus
from typing import List
from fastapi import FastAPI, HTTPException
from repositories.teacherRepository import TeacherRepository

from models.Teacher import Teacher
from models.Student import Student
from models.Classroom import Classroom
from repositories.teacherRepository import TeacherRepository
from repositories.studentRepository import StudentRepository
from repositories.classroomRepository import ClassroomRepository

app = FastAPI()

teacher_repo = TeacherRepository()
student_repo = StudentRepository()
classroom_repo = ClassroomRepository()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# CRUD Teacher
@app.get("/teachers", response_model=List[Teacher])
def get_teachers():
    return teacher_repo.read_all()

@app.get("/teachers/quantidade")
def get_teachers_count():
    quantidade = teacher_repo.count()
    return {"quantidade": quantidade}

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

@app.get("/students/quantidade")
def get_students_count():
    quantidade = student_repo.count()
    return {"quantidade": quantidade}

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

# CRUD Classroom
@app.get("/classrooms", response_model=List[Classroom])
def get_classrooms():
    return classroom_repo.read_all()

@app.get("/classrooms/quantidade")
def get_classrooms_count():
    quantidade = classroom_repo.count()
    return {"quantidade": quantidade}

@app.get("/classrooms/{classroom_id}", response_model=Classroom)
def get_classroom(classroom_id: int):
    classroom = classroom_repo.get_by_id(classroom_id)
    if not classroom:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Classroom not found")
    return classroom

@app.post("/classrooms", response_model=Classroom, status_code=HTTPStatus.CREATED)
def create_classroom(classroom: Classroom):
    result = classroom_repo.create(classroom)
    if not result:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="Classroom already exists")
    return result

@app.put("/classrooms/{classroom_id}", response_model=Classroom, status_code=HTTPStatus.OK)
def update_classroom(classroom_id: int, new_classroom: Classroom):
    result = classroom_repo.update(classroom_id, new_classroom)
    if not result:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Classroom not found")
    return result

@app.delete("/classrooms/{classroom_id}", status_code=HTTPStatus.OK)
def delete_classroom(classroom_id: int):
    result = classroom_repo.delete(classroom_id)
    if not result:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Classroom not found")
    return {"message": "Classroom deleted successfully"}