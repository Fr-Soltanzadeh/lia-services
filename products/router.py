from fastapi import APIRouter, status, HTTPException
from .schema import Product
from typing import List, Any


router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=List[Product])
def get_products() -> Any:
    ...


@router.get("/{product_id}", response_model=Product)
def get_product_by_id(product_id: int) -> Any:
    ...


@router.post("/", response_model=Product)
def post_product() -> Any:
    ...


@router.put("/{product_id}", response_model=Product)
def change_product_by_id(product_id: int) -> Any:
    ...


@router.delete("/{product_id}")
def delete_product_by_id(product_id: int) -> None:
    ...