import uvicorn
from fastapi import (
    FastAPI, Path, Query, Request, Body)
from typing import Optional

app = FastAPI()

@app.get('/')
async def index():
    return {"message": "Hello, worldy!"}

@app.get('/{name}/{id}')
async def user(name: str, id: int):
    return {"name": name, "id": id}

@app.get('/employee/{name}/{age}')
async def employee(name: str, age: int):
    return {"name": name, "age": age}

@app.get('/employee/{name}')
async def get_employee(name: str, age: int = 20):
    return {"name": name, "age": age}

@app.get('/employee/{name}/branch/{branch_id}')
async def get_employee_branch(branch_id:int, name:str=Path(min_length=5), 
                              brname:str=Query(None, min_length=5, max_length=10), 
                              age:Optional[int] = None):
    employee = {"name": name, 'Branch': brname, 
                'Branch_id': branch_id, 'Age': age}
    return employee

@app.post("/product")
async def add_new(request: Request, prodId:int = Body(),
                  prodName: str = Body(), price: float = Body(),
                  stock: int = Body()):
    product = {'Product ID': prodId, 'Product Name': prodName,
               'Price': price, 'Stock': stock}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)