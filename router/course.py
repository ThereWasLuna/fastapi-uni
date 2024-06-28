from fastapi import APIRouter, Response, status
from models.course import Course
from database.repo.course import insert_course, quary_course, replace_course, remove_course
from utils.validators import validator_course

course_router = APIRouter()

@course_router.get("/course/get/{stid}")
async def get_course(cid:str, res: Response):
    valid, data, errors = await quary_course(cid)
    res.status_code = status.HTTP_200_OK if valid else status.HTTP_400_BAD_REQUEST
    return {"status": valid, "data": data, "errors": errors}

@course_router.post("/course/register")
async def register_course(course: Course, res: Response) :
    valid, errors = validator_course(course)
    if valid:
        valid, errors = await insert_course(course.db())
    res.status_code = status.HTTP_201_CREATED if valid else status.HTTP_400_BAD_REQUEST
    return {"status": valid, "errors": errors}

@course_router.put("/course/update")
async def update_course(course: Course, res: Response):
    valid, errors = await validator_course(course)
    data = {}
    if valid:
        valid, data, errors = await replace_course(course)
    res.status_code = status.HTTP_202_ACCEPTED if valid else status.HTTP_400_BAD_REQUEST
    return {"status": valid, "data": data, "errors": errors}

@course_router.delete("/course/delete/{stid}")
async def delete_course(cid:str, res: Response):
    valid, errors = await remove_course(cid)
    res.status_code = status.HTTP_200_OK if valid else status.HTTP_400_BAD_REQUEST
    return {"status": valid, "errors": errors}