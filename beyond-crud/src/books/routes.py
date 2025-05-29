from fastapi import APIRouter, status, HTTPException
from books.book_data import books
from typing import List
from books.schemas import Book, UpdateBook

book_router = APIRouter()


@book_router.get("/", response_model=List[Book])
async def get_books() -> dict:
    return books


@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(book: Book) -> dict:
    # book.model_dump() # Uncomment this line if you want to see the raw data being processed
    books.append(book)
    return book


@book_router.get("/{book_id}", response_model=Book)
async def get_book(book_id: str) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@book_router.put("/{book_id}")
async def update_book(book_id: str, update_book: UpdateBook) -> dict:
    for book in books:
        if book["id"] == book_id:
                book["title"] = update_book.title
                book["author"] = update_book.author
                book["description"] = update_book.description
                book["level"] = update_book.level
                book["date_published"] = update_book.date_published
                book["status"] = update_book.status
                return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@book_router.delete("/{book_id}")
async def delete_book(book_id: str) -> dict:
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
