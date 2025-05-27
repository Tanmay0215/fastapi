from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {1: {"name": "John Doe", "age": 20, "grade": "A"}}


class Student(BaseModel):
    name: str
    age: int
    grade: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    grade: Optional[str] = None


@app.get("/")
def index():
    return {"Hello": "World"}


# @app.get("/get-students/{student_id}")
# def get_student(student_id: int):
#     return students[student_id]


@app.get("/get-students/{student_id}")
def get_student(
    student_id: int = Path(..., title="The ID of the student to retrieve", ge=1)
):
    return students[student_id]


# None means it is optional
# age: Optional[str] = None
# non default parameters cannot follow default parameters


@app.get("/get-by-name")
def get_students(name: str, age: int = None):
    for student_id in students:
        if students[student_id]["name"] == name and (
            age is None or students[student_id]["age"] == age
        ):
            return students[student_id]
    return {"data": "Not Found"}


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"error": "Student ID already exists"}
    students[student_id] = {
        "name": student.name,
        "age": student.age,
        "grade": student.grade,
    }
    return students[student_id]


@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"error": "Student not found"}
    if student.name is not None:
        students[student_id]["name"] = student.name
    if student.age is not None:
        students[student_id]["age"] = student.age
    if student.grade is not None:
        students[student_id]["grade"] = student.grade
    return students[student_id]


@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "Student not found"}
    del students[student_id]
    return {"message": "Student deleted successfully"}
