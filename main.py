from fastapi import FastAPI

from routers.class_router import router as class_router
from routers.student_router import router as student_router
from routers.teacher_router import router as teacher_router
from utils.logger import logger

app = FastAPI()

logger.info('Starting FastAPI application')

app.include_router(teacher_router)
app.include_router(student_router)
app.include_router(class_router)
