from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv


load_dotenv()


uri = os.getenv("MONGO_URI")

client = MongoClient(uri)

db = client.todo_db

collection_name = db["todo_collection"]

try:
    client.admin.command("ping")
    print("MongoDB connection successful")

except Exception as e:
    print(f"MongoDB connection failed: {e}")
