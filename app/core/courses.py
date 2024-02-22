

from pymongo import ReturnDocument
from app.models.courses import Courses



async def get_all(dbconn):
    collection = dbconn["courses"]
    result = [doc async for doc in collection.find({})]
    return result

async def get_by_id(_id, dbconn):
    collection = dbconn["courses"]
    result = await collection.find_one({"_id": _id})
    return result


async def create(course: Courses, dbconn):
    collection = dbconn["courses"]
    result = await collection.insert_one(course.dict())
    return "Course Created"


async def update(_id, course: Courses, dbconn):
    _course = {
        k: v for k, v in course.model_dump(by_alias=True).items() if v is not None
    }
    collection = dbconn["courses"]
    result = await collection.find_one_and_update({"_id": _id}, 
                                                  {"$set": _course},
                                                   return_document=ReturnDocument.AFTER)
    return "Course Updated"