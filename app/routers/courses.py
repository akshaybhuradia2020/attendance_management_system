
from fastapi import APIRouter, Depends
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient


from app.core.courses import *
from app.models.courses import Courses
from app.utility.dbconn import get_db

router = APIRouter(
    prefix="/courses"
)

@router.post("/create_course")
async def create_course(course: Courses, db: AsyncIOMotorClient= Depends(get_db)):
    res = await create(course, db)
    res

@router.get("/get_specific_course", response_model=Courses)
async def specific_course(_id, db: AsyncIOMotorClient= Depends(get_db)):
    res = await get_by_id(ObjectId(_id), db)
    return res

@router.get("/get_all_course", response_model=list[Courses])
async def all_course(db: AsyncIOMotorClient= Depends(get_db)):
    res = await get_all(db)
    return res


@router.post("/update_course")
async def update_course(_id, course: Courses, db:AsyncIOMotorClient=Depends(get_db)):
    res = await update(ObjectId(_id), course, db)
    return res