
from fastapi import FastAPI
from app.routers import attendance, courses, departments, students, users, login



app = FastAPI()



app.include_router(departments.router)
app.include_router(students.router)
app.include_router(users.router)
app.include_router(attendance.router)
app.include_router(courses.router)
app.include_router(login.router)

@app.get("/")
async def root():
    return {"message": "AMS is Up"}


