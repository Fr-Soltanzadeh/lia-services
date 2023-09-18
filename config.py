from fastapi import FastAPI
from products.router import router as product_router
from db_setting import init_db

app = FastAPI()

app.include_router(product_router)


@app.on_event("startup")
async def start_db():
    await init_db()


@app.get("/", tags=["Root"])
async def index() -> dict:
    return {"message": "Welcome to product app"}
