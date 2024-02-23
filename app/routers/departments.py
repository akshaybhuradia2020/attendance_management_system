
from fastapi import APIRouter, Depends
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient


from app.core.departments_operation import *
from app.models.departsments import Departments
from app.utility.dbconn import get_db
from app.utility.gen_check_jwt import verify_token


router = APIRouter(
    prefix="/departments"
)

@router.post("/create_department")
async def create_department(department: Departments, db: AsyncIOMotorClient = Depends(get_db), 
                            chk_tk: bool = Depends(verify_token)):
    if chk_tk:
        res = await create(department, db)
        return res
    

@router.get("/get_specific_department", response_model=Departments)
async def specific_department(_id, db: AsyncIOMotorClient = Depends(get_db), 
                              chk_tk: bool = Depends(verify_token)):
    if chk_tk:
        res = await get_by_id(ObjectId(_id), db)
        return res

@router.get("/get_all_department", response_model=list[Departments])
async def all_department(db: AsyncIOMotorClient = Depends(get_db),
                         chk_tk: bool = Depends(verify_token)):
    if chk_tk:
        res = await get_all(db)
        return res

@router.post("/update_department")
async def update_department(_id, department: Departments, db:AsyncIOMotorClient=Depends(get_db),
                           chk_tk: bool = Depends(verify_token)):
    if chk_tk:
        res = await update(ObjectId(_id), department, db)
        return res