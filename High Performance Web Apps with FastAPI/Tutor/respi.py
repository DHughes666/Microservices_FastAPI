from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI, Request, Response, Form, Cookie
from fastapi.templating import Jinja2Templates

app = FastAPI()
template = Jinja2Templates(directory="templates")

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

@app.post("/setcookie/")
async def set_cookie(
    request: Request, response: Response, user:str=Form(...),
    pwd:str=Form(...)):
    response.set_cookie(key="user", value=user)
    return {'message': "Hello, world!"}

@app.get("/", response_class=HTMLResponse)
async def index(request: Request, user:str=Cookie(None)):
    return template.TemplateResponse(
        "form2.html", {"request": request, "user": user})

@app.get("/header/")
async def set_header():
    content = {"message": "Hello, world!"}
    headers = {"X-Web-Framework": "FastAPI", 
               "Content-Language": "en-US"}
    return JSONResponse(content=content, headers = headers)

if __name__ == '__main__':
    uvicorn.run("respi:app", host="0.0.0.0", port=8000, reload=True)