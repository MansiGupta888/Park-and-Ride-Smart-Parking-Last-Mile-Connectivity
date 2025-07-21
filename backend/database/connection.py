# backend/database/connection.py
from motor.motor_asyncio import AsyncIOMotorClient

client = None

def get_db():
    return client.park_and_ride

async def connect_to_mongo():
    global client
    client = AsyncIOMotorClient("mongodb://localhost:27017")
