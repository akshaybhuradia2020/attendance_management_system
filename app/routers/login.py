from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.login import *
from app.models.login import Login
from app.utility.dbconn import get_db

router = APIRouter(
    prefix=""
)

@router.post("/login")
async def check_user_cred(usercred: Login ,db: AsyncIOMotorClient = Depends(get_db)):
    res = await login(usercred, db)
    return res