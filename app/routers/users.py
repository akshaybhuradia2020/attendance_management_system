
from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from app.models.users import Users
from app.utility.dbconn import get_db
from app.core.users_operations import *

router = APIRouter(
    prefix="/users"
)

@router.post("/create_user")
async def create_user(user: Users, db:AsyncIOMotorClient=Depends(get_db)):
    res = await create(user, db)
    return res

@router.get("/get_specific_user", response_model=Users)
async def specific_user(_id, db:AsyncIOMotorClient= Depends(get_db)):
    res = await get_by_id(ObjectId(_id), db)
    return res

@router.get("/get_all_user", response_model=list[Users])
async def all_user(db:AsyncIOMotorClient=Depends(get_db)):
    res = await get_all(db)
    return res

@router.post("/update_user")
async def update_user(_id, user: Users, db:AsyncIOMotorClient=Depends(get_db)):
    res = await update(ObjectId(_id), user, db)
    return res