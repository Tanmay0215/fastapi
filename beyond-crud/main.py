from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.get("/greet/{name}")
async def greet(name: str) -> dict:
    return {"message": f"Hello {name}, welcome to the FastAPI application!"}


# by default, it will use the query parameter
# non default parameters cannot follow default parameters


@app.get("/greet")
async def greet(name: Optional[str] = "User", age: int = 0) -> dict:
    return {"message": f"Hello {name}, welcome to the FastAPI application!"}


class Book(BaseModel):
    title: str
    author: str


# data in the request body
@app.post("/create-book")
async def create_book(book: Book) -> dict:
    return {
        "title": book.title,
        "author": book.author,
    }

@app.get("/get-headers", status_code=200)
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None)
):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent

    return request_headers