import pytest

from tests.conftest import base_url
from products.schema import Product


async def test_get_products(test_client):
    #setup
    product = Product(
        _id="65094ff97a289963b080eef1", name="test", price=1, description="test"
    )
    await product.insert()
    #test
    response = await test_client.get(f"{base_url}/products/")
    response_json = response.json()
    assert response.status_code == 200
    assert len(response_json) == 1


async def test_create_product_success(test_client):
    payload = {"name": "prod", "price": 1, "description": "d"}
    response = await test_client.post(f"{base_url}/products/", json=payload)
    response_json = response.json()
    assert response_json["name"] == "prod"
    assert response.status_code == 201


async def test_create_product_invalid_input(test_client):
    payload = {"name": "prod", "description": "d"}
    response = await test_client.post(f"{base_url}/products/", json=payload)
    assert response.status_code == 422


async def test_get_product_success(test_client):
    #setup
    product = Product(
        _id="65094ff97a289963b080eef1", name="test", price=1, description="test"
    )
    await product.insert()
    product_id = product.id
    #test
    response = await test_client.get(f"{base_url}/products/{product_id}")
    response_json = response.json()
    assert response_json["name"] == "test"
    assert response.status_code == 200


async def testgete_product_not_exist(test_client):
    product_id = "65094ff97a289963b080eef1"
    response = await test_client.get(f"{base_url}/products/{product_id}")
    assert response.status_code == 404


async def test_get_invalid_input(test_client):
    product_id = "1"
    response = await test_client.get(f"{base_url}/products/{product_id}")
    assert response.status_code == 422


async def test_update_product_success(test_client):
    #setup
    product = Product(
        _id="65094ff97a289963b080eef1", name="test", price=1, description="test"
    )
    await product.insert()
    product_id = product.id
    #test
    payload = {"price": 2}
    response = await test_client.put(f"{base_url}/products/{product_id}", json=payload)
    response_json = response.json()
    assert response_json["price"] == 2
    assert response.status_code == 200


async def test_update_product_not_exist(test_client):
    product_id = "65094ff97a289963b080eef2"
    payload = {"price": 2}
    response = await test_client.put(f"{base_url}/products/{product_id}", json=payload)
    assert response.status_code == 404


async def test_update_invalid_input(test_client):
    product_id = "1"
    response = await test_client.put(f"{base_url}/products/{product_id}")
    assert response.status_code == 422


async def test_delete_product_not_exist(test_client):
    product_id = "65094ff97a289963b080eef2"
    response = await test_client.delete(f"{base_url}/products/{product_id}")
    assert response.status_code == 404


async def test_delete_invalid_input(test_client):
    product_id = "1"
    response = await test_client.delete(f"{base_url}/products/{product_id}")
    assert response.status_code == 422


async def test_delete_product_success(test_client):
    #setup
    product = Product(
        _id="65094ff97a289963b080eef1", name="test", price=1, description="test"
    )
    await product.insert()
    product_id = product.id
    #test
    response = await test_client.delete(f"{base_url}/products/{product_id}")
    assert response.status_code == 204
