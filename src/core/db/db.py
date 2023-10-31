from motor.motor_asyncio import AsyncIOMotorClient

from src.core.config.db import settings_db


client = AsyncIOMotorClient(settings_db.database_url)
db = client.get_database(settings_db.MONGO_DB)
