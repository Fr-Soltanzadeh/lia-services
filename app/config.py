from os import getenv
from dotenv import load_dotenv
from pydantic import BaseModel


load_dotenv(dotenv_path=".env")

class Settings(BaseModel):
    """Server config settings"""

    hostname: str = getenv("hostname")
    port: int = int(getenv("port"))
    mongodb_uri: str = getenv("MongoDB_URI")
    db_name: str = getenv("database_name")

CONFIG = Settings()
