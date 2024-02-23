
from app.models.login import Login
from app.utility.gen_check_jwt import generate_token


async def login(usercred: Login, dbconn):
    collection = dbconn["users"]
    result = await collection.find_one({"username": usercred.username, "password": usercred.passwd})
    if result == None:
        return {"token": None}
    return {"token": generate_token({"username": usercred.username, "password": usercred.passwd}), 
            "token_type": "bearer"}