from fastapi import APIRouter, Response, status
from models.student import Student
from database.repo.student import insert_student, quary_student, replace_student, remove_student, inster_student_course, remove_student_course
from utils.validators import validator_student

student_router = APIRouter()

@student_router.get("/student/get/{stid}")
async def get_student(stid:str, res: Response):
    valid, data, errors = await quary_student(stid)
    res.status_code = status.HTTP_200_OK if valid else status.HTTP_400_BAD_REQUEST
    return {"status": valid, "data": data, "errors": errors}

@student_router.post("/student/register")
async def register_student(student: Student, res: Response) :
    valid, errors = validator_student(student)
    if valid:
        valid, errors = await insert_student(student.db())
    res.status_code = status.HTTP_201_CREATED if valid else status.HTTP_400_BAD_REQUEST
    return {"status": valid, "errors": errors}

@student_router.put("/student/update")
async def update_student(student: Student, res: Response):
    valid, errors = await validator_student(student)
    data = {}
    if valid:
        valid, data, errors = await replace_student(student)
    res.status_code = status.HTTP_202_ACCEPTED if valid else status.HTTP_400_BAD_REQUEST
    return {"status": valid, "data": data, "errors": errors}

@student_router.delete("/student/delete/{stid}")
async def delete_student(stid:str, res: Response):
    valid, errors = await remove_student(stid)
    res.status_code = status.HTTP_200_OK if valid else status.HTTP_400_BAD_REQUEST
    return {"status": valid, "errors": errors}

@student_router.put("/student/course/{stid}/{cid}")
async def add_student_course(stid:str, cid:str, res: Response):
    valid, errors = await inster_student_course(stid, cid)
    res.status_code = status.HTTP_201_CREATED if valid else status.HTTP_400_BAD_REQUEST
    return {"status": valid, "errors": errors}

@student_router.delete("/student/course/{stid}/{cid}")
async def delete_student_course(stid:str, cid:str, res: Response):
    valid, errors = await remove_student_course(stid, cid)
    res.status_code = status.HTTP_202_ACCEPTED if valid else status.HTTP_400_BAD_REQUEST
    return {"status": valid, "errors": errors}