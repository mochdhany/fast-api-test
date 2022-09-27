
from fastapi import FastAPI
from myrouter import student_router

app = FastAPI()
@app.get("/")
async def hello() -> dict:
    return {
        "message": "Dhany"
    }

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
app.include_router(student_router)