from app.models.students import Students
from pymongo import ReturnDocument


async def get_all(dbconn):
    collection = dbconn["students"]
    result = [doc async for doc in collection.find({})]
    return result

async def get_by_id(_id, dbconn):
    collection = dbconn["students"]
    result = await collection.find_one({"_id": _id})
    return result


async def create(student: Students, dbconn):
    collection = dbconn["students"]
    result = await collection.insert_one(student.dict())
    return "Student Created"

async def update(_id, student: Students, dbconn):
    _student = {
        k: v for k, v in student.model_dump(by_alias=True).items() if v is not None
    }
    collection = dbconn["students"]
    result = await collection.find_one_and_update({"_id": _id}, 
                                                  {"$set": _student},
                                                   return_document=ReturnDocument.AFTER)
    return "Student Updated"