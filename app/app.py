from fastapi import FastAPI

from products.router import router as product_router
from db_setting import init_db
from config import CONFIG


app = FastAPI()
app.include_router(product_router)


@app.on_event("startup")
async def start_db():
    await init_db(CONFIG.db_name)


@app.get("/", tags=["Root"])
async def index() -> dict:
    return {"message": "Welcome to product app"}
