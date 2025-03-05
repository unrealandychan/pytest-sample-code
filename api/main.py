from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


db = {
    1: "eddie",
    2: "james",
    3: "john"
}

class User(BaseModel):
    id: int
    username: str
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/{user_id}")
async def user(user_id):
    return db[user_id]

@app.get("/users")
async def users():
    return db

@app.post("/users")
async def create_users(user: User):
    db[user.id] = user.username
    return db[user.id]