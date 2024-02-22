# import uvicorn
from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Things Fall Apart', 'author': 'Chinua Achebe'},
    'book_2': {'title': 'After Death', 'author': 'Dean Koontz'},
    'book_3': {'title': 'Physics of the Impossible', 'author': 'Michio Kaku'},
    'book_4': {'title': 'Hacking Darwin', 'author': 'Jamie Metzl'},
    'book_5': {'title': 'Zero Hour', 'author': 'David Baldacci'},
    'book_6': {'title': 'Contagion', 'author': 'Robin Cook'},
}

class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"


@app.get("/")
async def first_api():
    return {"message": "Hello, worldyy!"}

@app.get("/books")
async def read_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS

@app.get("/{book_name}")
async def read_book(book_name: str):
    return BOOKS[book_name]

@app.post("/new_book")
async def create_book(book_title, book_author: str):
    current_book_id = 0
    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split('_')[-1])
            if x > current_book_id:
                current_book_id = x
    BOOKS[f'book_{current_book_id + 1}'] = {'title': book_title, 
                                            'author': book_author}
    return BOOKS

@app.put('/{book_name}')
async def update_book(book_name, book_title, book_author: str):
    book_info = {'title': book_title, 'author': book_author}
    BOOKS[book_name] = book_info
    return BOOKS

@app.delete('/{book_name}')
async def delete_book(book_name):
    del BOOKS[book_name]
    return f'Book_{book_name} has been deleted'

@app.get("/direction/{direction_name}")
async def read_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {"Direction": direction_name, "sub": "Up"}
    if direction_name == DirectionName.south:
        return {"Direction": direction_name, "sub": "Down"}
    if direction_name == DirectionName.east:
        return {"Direction": direction_name, "sub": "Right"}
    if direction_name == DirectionName.west:
        return {"Direction": direction_name, "sub": "Left"}

@app.get("/books/mybook")
async def read_favorite_book():
    return {"book_title": "My Favorite Book"}



# if __name__ == '__main__':
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)