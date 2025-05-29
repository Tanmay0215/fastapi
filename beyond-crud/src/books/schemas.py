from pydantic import BaseModel
from typing import Optional


class Book(BaseModel):
    id: str
    title: str
    author: str
    description: str
    level: str
    date_published: str
    status: str


class UpdateBook(BaseModel):
    id: str
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    level: Optional[str] = None
    date_published: Optional[str] = None
    status: Optional[str] = None
