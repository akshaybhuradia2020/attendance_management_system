

from pymongo import ReturnDocument
from app.models.users import Users



async def get_all(dbconn):
    collection = dbconn["users"]
    result = [doc async for doc in collection.find({})]
    return result

async def get_by_id(_id, dbconn):
    collection = dbconn["users"]
    result = await collection.find_one({"_id": _id})
    return result


async def create(user: Users, dbconn):
    collection = dbconn["users"]
    result = await collection.insert_one(user.dict())
    return "User Created"


async def update(_id, user: Users, dbconn):
    _user = {
        k: v for k, v in user.model_dump(by_alias=True).items() if v is not None
    }
    collection = dbconn["users"]
    result = await collection.find_one_and_update({"_id": _id}, 
                                                  {"$set": _user},
                                                   return_document=ReturnDocument.AFTER)
    return "User Updated"