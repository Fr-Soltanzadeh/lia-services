from beanie import init_beanie
import motor.motor_asyncio

from products.schema import Product


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://localhost:27017"
    )

    await init_beanie(database=client.test_db, document_models=[Product])