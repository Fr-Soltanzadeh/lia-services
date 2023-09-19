from pydantic import BaseModel
from typing import Optional
from beanie import Document


class Product(Document):
    name: str
    price: float
    description: str

    class DocumentMeta:
        name = "products_collection"


class ProductInCreate(BaseModel):
    name: str
    price: float
    description: str


class ProductInUpdate(BaseModel):
    name: Optional[str]=None
    price: Optional[float]=None
    description: Optional[str]=None
