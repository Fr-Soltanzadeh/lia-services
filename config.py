from fastapi import FastAPI
from products.router import router as product_router


app = FastAPI()

app.include_router(product_router)


@app.get("/")
async def hello():
    return {"message": "Hello World"}
