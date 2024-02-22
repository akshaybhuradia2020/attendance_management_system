
from pymongo import ReturnDocument
from app.models.mark_attendance import Attendance_Log



async def get_all(dbconn):
    collection = dbconn["mark_attendance"]
    result = [doc async for doc in collection.find({})]
    return result

async def get_by_id(_id, dbconn):
    collection = dbconn["mark_attendance"]
    result = await collection.find_one({"_id": _id})
    return result


async def create(attendance: Attendance_Log, dbconn):
    collection = dbconn["mark_attendance"]
    result = await collection.insert_one(attendance.dict())
    return "Attendance Created"

async def update(_id, user: Attendance_Log, dbconn):
    _attendance = {
        k: v for k, v in user.model_dump(by_alias=True).items() if v is not None
    }
    collection = dbconn["mark_attendance"]
    result = await collection.find_one_and_update({"_id": _id}, 
                                                  {"$set": _attendance},
                                                   return_document=ReturnDocument.AFTER)
    return "Attendance Updated"