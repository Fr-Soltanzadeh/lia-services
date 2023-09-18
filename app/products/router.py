from fastapi import APIRouter, status, HTTPException
from beanie import PydanticObjectId
from .schema import Product, UpdateProduct
from typing import List, Any
from utils import encode_input


router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=List[Product])
async def get_products():
    products=await Product.find_all().to_list()
    return products


@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: PydanticObjectId):
    product = await Product.get(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {product_id} not found")
    return product


@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    await product.insert()
    return product


@router.put("/{product_id}", response_model=Product)
async def update_product(product_id: PydanticObjectId, updated_product: UpdateProduct):
    product = await Product.get(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {product_id} not found")
    await product.update({"$set": encode_input(updated_product)})
    return product


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: PydanticObjectId):
    product = await Product.get(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {product_id} not found")
    await product.delete()
    return {"message": f"Product with id {product_id} deleted successfully"}