from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()

class Product(BaseModel):
    prodId: int
    prodName: str
    price: float
    stock: int
    inventory_val: float

class ProductVal(BaseModel):
    prodId: int
    prodName: str
    inventory_val: float

@app.post("/product/", response_model=ProductVal)
async def add_new(product: Product):
    product.inventory_val = product.price * product.stock
    return product

if __name__ == '__main__':
    uvicorn.run("respi:app", host="0.0.0.0", port=8000, reload=True)