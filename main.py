from fastapi import FastAPI
from routers.teacher_router import router as teacher_router
from routers.student_router import router as student_router
from routers.classroom_router import router as classroom_router
from routers.class_router import router as class_router

app = FastAPI()

app.include_router(teacher_router)
app.include_router(student_router)
app.include_router(classroom_router)
app.include_router(class_router)