from pymongo import ReturnDocument
from app.models.departsments import Departments



async def get_all(dbconn):
    collection = dbconn["departments"]
    result = [doc async for doc in collection.find({})]
    return result

async def get_by_id(_id, dbconn):
    collection = dbconn["departments"]
    result = await collection.find_one({"_id": _id})
    return result


async def create(department: Departments, dbconn):
    collection = dbconn["departments"]
    result = await collection.insert_one(department.dict())
    return "Department Created"


async def update(_id, department: Departments, dbconn):
    _department = {
        k: v for k, v in department.model_dump(by_alias=True).items() if v is not None
    }
    collection = dbconn["departments"]
    result = await collection.find_one_and_update({"_id": _id}, 
                                                  {"$set": _department},
                                                   return_document=ReturnDocument.AFTER)
    return "Department Updated"