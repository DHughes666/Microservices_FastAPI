# import uvicorn
from fastapi import FastAPI

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Things Fall Apart', 'author': 'Chinua Achebe'},
    'book_2': {'title': 'After Death', 'author': 'Dean Koontz'},
    'book_3': {'title': 'Physics of the Impossible', 'author': 'Michio Kaku'},
    'book_4': {'title': 'Hacking Darwin', 'author': 'Jamie Metzl'},
    'book_5': {'title': 'Zero Hour', 'author': 'David Baldacci'},
    'book_6': {'title': 'Contagion', 'author': 'Robin Cook'},
}


@app.get("/")
async def first_api():
    return {"message": "Hello, worldyy!"}

@app.get("/books")
async def read_all_books():
    return BOOKS



# if __name__ == '__main__':
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)