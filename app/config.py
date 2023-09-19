from fastapi import FastAPI
from os import getenv
from dotenv import load_dotenv

from products.router import router as product_router
from db_setting import init_db


app = FastAPI()

app.include_router(product_router)

load_dotenv(dotenv_path=".env")
hostname=getenv("hostname")
port=int(getenv("port"))
mongodb_uri=getenv("MongoDB_URI")

@app.on_event("startup")
async def start_db():
    await init_db(getenv("database_name"))


@app.get("/", tags=["Root"])
async def index() -> dict:
    return {"message": "Welcome to product app"}
