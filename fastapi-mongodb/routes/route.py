from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos


@router.post("/", status_code=201)
async def create_todo(todo: Todo):
    collection_name.insert_one(dict(todo))


@router.get("/{todo_id}")
async def get_todo(todo_id: str):
    todo = collection_name.find_one({"_id": ObjectId(todo_id)})


@router.put("/{todo_id}")
async def update_todo(todo_id: str, todo: Todo):
    collection_name.find_one_and_update(
        {"_id": ObjectId(todo_id)},
        {"$set": dict(todo)},
    )


@router.delete("/{todo_id}")
async def delete_todo(todo_id: str):
    collection_name.delete_one({"_id": ObjectId(todo_id)})
