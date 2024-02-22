from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

BOOKS = []

@app.get('/books')
async def read_all_books():
    return BOOKS