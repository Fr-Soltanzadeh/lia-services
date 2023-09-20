from beanie import init_beanie
from typing import Generator
import pytest
from mongomock_motor import AsyncMongoMockClient
from httpx import AsyncClient

from config import CONFIG
from products.schema import Product
from app import app


"""
Pytest fixtures
"""

base_url="http://127.0.0.1"


@pytest.fixture(autouse=True)
async def get_test_db():
    client = AsyncMongoMockClient()
    await init_beanie(document_models=[Product], database=client.get_database(name="test_db"))


@pytest.fixture(autouse=True)
def anyio_backend():
    return 'asyncio'


@pytest.fixture(autouse=True)
async def test_client(get_test_db) -> Generator:
    async with AsyncClient(app=app) as client:
        yield client