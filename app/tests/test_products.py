import pytest

from tests.conftest import base_url


@pytest.mark.asyncio
async def test_get_products(test_client):

    response = await test_client.get(f"{base_url}/products/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_product(test_client):

    payload={"name":"prod", "price":1, "description":"d"}
    response = await test_client.post(f"{base_url}/products/",json=payload)
    response_json = response.json()
    assert response_json["name"] == "prod"
    assert response.status_code == 201

