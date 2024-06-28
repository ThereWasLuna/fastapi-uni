from fastapi import APIRouter, Response, status
from models.head import Head
from database.repo.head import insert_head, quary_head, replace_head, remove_head, insert_head_course, remove_head_course
from utils.validators import validator_head

head_router = APIRouter()

@head_router.get("/head/get/{stid}")
async def get_head(lid:str, res: Response):
    valid, data, errors = await quary_head(lid)
    res.status_code = status.HTTP_200_OK if valid else status.HTTP_400_BAD_REQUEST
    return {"status": valid, "data": data, "errors": errors}

@head_router.post("/head/register")
async def register_head(head: Head, res: Response) :
    valid, errors = validator_head(head)
    if valid:
        valid, errors = await insert_head(head.db())
    res.status_code = status.HTTP_201_CREATED if valid else status.HTTP_400_BAD_REQUEST
    return {"status": valid, "errors": errors}

@head_router.put("/head/update")
async def update_head(head: Head, res: Response):
    valid, errors = await validator_head(head)
    data = {}
    if valid:
        valid, data, errors = await replace_head(head)
    res.status_code = status.HTTP_202_ACCEPTED if valid else status.HTTP_400_BAD_REQUEST
    return {"status": valid, "data": data, "errors": errors}

@head_router.delete("/head/delete/{stid}")
async def delete_head(lid:str, res: Response):
    valid, errors = await remove_head(lid)
    res.status_code = status.HTTP_200_OK if valid else status.HTTP_400_BAD_REQUEST
    return {"status": valid, "errors": errors}

@head_router.put("/head/course/{stid}/{cid}")
async def add_head_course(lid:str, cid:str, res: Response):
    valid, errors = await insert_head(lid, cid)
    res.status_code = status.HTTP_201_CREATED if valid else status.HTTP_400_BAD_REQUEST
    return {"status": valid, "errors": errors}

@head_router.put("/head/course/{stid}/{cid}")
async def delete_head_course(lid:str, cid:str, res: Response):
    valid, errors = await remove_head_course(lid, cid)
    res.status_code = status.HTTP_202_ACCEPTED if valid else status.HTTP_400_BAD_REQUEST
    return {"status": valid, "errors": errors}