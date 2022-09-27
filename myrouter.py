from fastapi import APIRouter
from pydantic import BaseModel
class TheStudent(BaseModel):
    id: int
    name: str

student_router = APIRouter()
@student_router.get("/")
async def hello() -> dict:
    return {
    "message": "Hello World"
    }
student_list = [TheStudent(id=18220087,name="Mochammad Ramadhany"),TheStudent(id=18220696,name="John Die")]
@student_router.post("/student")
async def add_student(student: TheStudent) -> dict:
    student_list.append(student)
    return {"message": "Success"}
@student_router.get("/student")
async def get_student() -> dict:
    return {"student": student_list}