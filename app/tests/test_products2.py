# from fastapi.testclient import TestClient
# from products.schema import Product
# from beanie import init_beanie 
# import pytest
# from config import app
# from motor.motor_asyncio import AsyncIOMotorClient

# from fastapi import FastAPI
# from products.router import router as product_router
# from db_setting import init_db

# app = FastAPI()

# app.include_router(product_router)


# @app.on_event("startup")
# async def start_db():
#     await init_db("test_db")


# client=TestClient(app)

# init_beanie(database=AsyncIOMotorClient("mongodb://localhost:27017").test_db, document_models=[Product])

# def test_get_products():
#     response = client.get("/products/")
#     assert response.status_code == 200

# # def test_get_product(product_id):
# #     response = client.get(f"/products/{product_id}")
# #     assert response.status_code == 200

# # def test_delete_product(product_id):
# #     response = client.get(f"/products/{product_id}")
# #     assert response.status_code == 204

# import pytest
# from fastapi.testclient import TestClient
# from motor.motor_asyncio import AsyncIOMotorClient

# from config import app
# from products.schema import Product


# @pytest.fixture(scope="session")
# def test_db():
#     client = AsyncIOMotorClient("mongodb://localhost:27017")
#     yield client["test_db"]
#     client.drop_database("test_db")


# @pytest.fixture
# def test_client(test_db):
#     app.db = test_db
#     app.document_models = [Product]
#     client = TestClient(app)
#     return client
    

# def test_get_products(test_client):
#     # Insert test products into the database
#     test_client.app.db["products_collection"].insert_many([
#         {"name": "Product 1", "price": 10.0, "description": "Description 1"},
#         {"name": "Product 2", "price": 20.0, "description": "Description 2"},
#     ])
    
#     # Send a GET request to the /products endpoint
#     response = test_client.get("/products/")
    
#     # Assert that the response status code is 200 (OK)
#     assert response.status_code == 200
    
#     # Assert that the response body contains the expected products
#     assert len(response.json()) == 2
#     assert response.json()[0]["name"] == "Product 1"
#     assert response.json()[1]["name"] == "Product 2"


# # def test_create_product(test_client):
# #     # Send a POST request to the /products endpoint to create a new product
# #     response = test_client.post(
# #         "/products/",
# #         json={"name": "New Product", "price": 30.0, "description": "New Description"}
# #     )
    
# #     # Assert that the response status code is 201 (Created)
# #     assert response.status_code == 201
    
# #     # Assert that the response body contains the created product
# #     assert response.json()["name"] == "New Product"
# #     assert response.json()["price"] == 30.0
# #     assert response.json()["description"] == "New Description"


# # def test_update_product(test_client):
# #     # Insert a test product into the database
# #     product = {
# #         "name": "Product 1",
# #         "price": 10.0,
# #         "description": "Description 1"
# #     }
# #     product_id = test_client.app.db["products_collection"].insert_one(product).inserted_id
    
# #     # Send a PUT request to update the product
# #     response = test_client.put(
# #         f"/products/{product_id}",
# #         json={"name": "Updated Product", "price": 20.0, "description": "Updated Description"}
# #     )
    
# #     # Assert that the response status code is 200 (OK)
# #     assert response.status_code == 200
    
# #     # Assert that the response body contains the updated product
# #     assert response.json()["name"] == "Updated Product"
# #     assert response.json()["price"] == 20.0
# #     assert response.json()["description"] == "Updated Description"


# # def test_delete_product(test_client):
# #     # Insert a test product into the database
# #     product = {
# #         "name": "Product 1",
# #         "price": 10.0,
# #         "description": "Description 1"
# #     }
# #     product_id = test_client.app.db["products_collection"].insert_one(product).inserted_id
    
# #     # Send a DELETE request to delete the product
# #     response = test_client.delete(f"/products/{product_id}")
    
# #     # Assert that the response status code is 204 (No Content)
# #     assert response.status_code == 204
    
# #     # Assert that the product has been deleted from the database
# #     assert test_client.app.db["products_collection"].find_one({"_id": product_id}) is None


import pytest
import httpx
from fastapi import FastAPI
from fastapi.testclient import TestClient
from motor.motor_asyncio import AsyncIOMotorClient
from httpx import AsyncClient

from products.router import router
from db_setting import init_db
from products.schema import Product

# from .conftest import test_client
@pytest.mark.asyncio
async def test_read_main(client: AsyncClient):
    print(client.__dir__)
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to product app"}

# @pytest.fixture(scope="module")
# def client(test_app):
#     return TestClient(test_app)


# Tests for GET /products
@pytest.mark.asyncio
async def test_get_products(client: AsyncClient):

    response = await client.get("/products/")
    print(response)
    assert response.status_code == 201