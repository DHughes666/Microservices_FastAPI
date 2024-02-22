from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID
from enum import Enum
from typing import Optional

app = FastAPI()

class Book(BaseModel):
    id : UUID
    title : str = Field(min_length=2)
    author : str = Field(min_length=1, max_length=100)
    description : Optional[str] = Field(
        title="Description of the book",
        max_length=100,
        min_length=1
    )
    rating : int = Field(gt=-1, lt=101)

    class Config:
        json_schema_extra = {
            "example": {
                "id": "6b7829cd-3ece-4fe5-8ee4-234856b73f75",
                "title": "Consolations of Philosophy",
                "author": "Alain De Botton",
                "description": "I feared a lot of things growing up, most of which never happened",
                "rating": 89
            }
        }

BOOKS = []

@app.post("/new_book")
async def create_book(book: Book):
    BOOKS.append(book)
    return book

@app.get('/books')
async def read_all_books(books_to_return: Optional[int] = None):
    if len(BOOKS) < 1:
        create_books_no_api()
    if books_to_return and len(BOOKS) >= books_to_return > 0:
        i = 1
        new_books = []
        while i <= books_to_return:
            new_books.append(BOOKS[i - 1])
            i += 1
        return new_books
    return BOOKS

def create_books_no_api():
    book_1 = Book(id="670080c0-655d-4249-b5e6-eb38c53ecb73",
                  title="Upheaval",
                  author="Jared Diamond",
                  description="Pulling countries out of their depths",
                  rating=87)
    book_2 = Book(id="2f96cfcc-9b03-4438-91fb-e9b4803a5747",
                  title="The Spirit Level",
                  author="Richard Wilkinson",
                  description="Levelling the playing field",
                  rating=80)
    book_3 = Book(id="07249573-ce63-4727-a0b4-001bd234564c",
                  title="Hacking Darwin",
                  author="Jamie Metzl",
                  description="Taking control of our evolution",
                  rating=92)
    book_4 = Book(id="59265584-b27e-48a8-8f96-8803cf102138",
                  title="The Innovators",
                  author="Walter Isaacson",
                  description="The age of zeros and ones",
                  rating=98)
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)
