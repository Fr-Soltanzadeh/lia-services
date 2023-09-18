from pydantic import BaseModel
from typing import Optional
from beanie import Document


class Product(Document):
    name: str
    price: float
    description: str

    class Settings:
        name = "products_collection"


class UpdateProduct(BaseModel):
    name: Optional[str]
    price: Optional[float]
    description: Optional[str]