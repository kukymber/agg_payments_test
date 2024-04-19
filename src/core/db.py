import os

from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

client = AsyncIOMotorClient(f'mongodb://{DB_HOST}:{DB_PORT}')
db = client.new_database
salaries = db.new_collection
