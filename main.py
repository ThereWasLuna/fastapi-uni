from fastapi import FastAPI
from router.student import student_router
from router.head import head_router
from router.course import course_router

app = FastAPI()

app.include_router(student_router)
app.include_router(head_router)
app.include_router(course_router)