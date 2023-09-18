from pydantic import BaseModel
from beanie import Document


class Product(Document):
    name: str
    price: float
    description: str

    class Settings:
        name = "products_collection"