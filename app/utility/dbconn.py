from motor.motor_asyncio import AsyncIOMotorClient

from app.utility.const import DATABASE_NAME, DATABASE_URL

async def get_db():
    _client = AsyncIOMotorClient(DATABASE_URL)
    _db = _client[DATABASE_NAME]
    try:
        yield _db
    finally:
        _client.close()
