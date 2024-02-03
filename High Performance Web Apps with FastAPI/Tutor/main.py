import uvicorn
from fastapi import FastAPI
app = FastAPI()

@app.get('/')
async def index():
    return {"message": "Hello, worldy!"}

@app.get('/{name}/{id}')
async def user(name: str, id: int):
    return {"name": name, "id": id}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)