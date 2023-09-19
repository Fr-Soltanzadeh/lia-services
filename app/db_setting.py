from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from products.schema import Product


async def init_db(db_name):
    from config import mongodb_uri
    
    client = AsyncIOMotorClient(mongodb_uri)
    await init_beanie(database=client[db_name], document_models=[Product])