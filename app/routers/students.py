from fastapi import APIRouter, Depends
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.students_operation import *
from app.models.students import Students
from app.utility.dbconn import get_db

router = APIRouter(
    prefix="/students"
)

@router.post("/create_student")
async def create_student(student: Students, db: AsyncIOMotorClient = Depends(get_db)):
    res = await create(student, db)
    return res

@router.get("/get_specific_student", response_model=Students)
async def specific_student(_id, db: AsyncIOMotorClient= Depends(get_db)):
    res = await get_by_id(ObjectId(_id), db)
    return res

@router.get("/get_all_student", response_model=list[Students])
async def all_student(db: AsyncIOMotorClient= Depends(get_db)):
    res = await get_all(db)
    return res

@router.post("/update_student")
async def update_student(_id, student: Students, db:AsyncIOMotorClient=Depends(get_db)):
    res = await update(ObjectId(_id), student, db)
    return res