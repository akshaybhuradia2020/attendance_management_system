

from fastapi import APIRouter, Depends
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient


from app.core.mark_attendance import *
from app.models.mark_attendance import Attendance_Log
from app.utility.dbconn import get_db
from app.utility.gen_check_jwt import verify_token

router = APIRouter(
    prefix="/attendance"
)

@router.post("/mark_attendance")
async def mark_attendance(attendance: Attendance_Log, db: AsyncIOMotorClient= Depends(get_db),
                          chk_tk: bool = Depends(verify_token)):
    if chk_tk:
        res = await create(attendance, db)
        return res

@router.get("/get_specific_attendance", response_model=Attendance_Log)
async def specific_attendance(_id, db: AsyncIOMotorClient= Depends(get_db),
                              chk_tk: bool = Depends(verify_token)):
    if chk_tk:
        res = await get_by_id(ObjectId(_id), db)
        return res

@router.get("/get_all_attendance", response_model=list[Attendance_Log])
async def all_attendance(db: AsyncIOMotorClient= Depends(get_db),
                         chk_tk: bool = Depends(verify_token)):
    if chk_tk:
        res = await get_all(db)
        return res

@router.post("/update_attendance")
async def update_attendance(_id, attendance: Attendance_Log, db:AsyncIOMotorClient=Depends(get_db),
                            chk_tk: bool = Depends(verify_token)):
    if chk_tk:
        res = await update(ObjectId(_id), attendance, db)
        return res