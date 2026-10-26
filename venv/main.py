from fastapi import FastAPI
from routes import create_student, delete_student, get_student, update_student

app = FastAPI(
    title="Student Management System",
    description="FastAPI project with CRUD operations for students",
    version="1.0.0"
)

app.include_router(create_student.router)
app.include_router(get_student.router)
app.include_router(update_student.router)
app.include_router(delete_student.router)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the FastAPI Student Project!",
        "docs_url": "http://127.0.0.1:8000/docs"
    }