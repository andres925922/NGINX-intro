from fastapi import FastAPI, WebSocket
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from dataclasses import dataclass

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(f"Message text was: {data}")
        await websocket.send_text(f"Message text was: {data}")

@app.get("/health")
def health_check():
    return JSONResponse(content={"status": "ok"}, status_code=200)

@dataclass
class User:
    username: str
    user_id: int

users = [
    User(username="user1", user_id=1),
    User(username="user2", user_id=2),
    User(username="user3", user_id=3)
]

@app.get("/users")
def get_users():
    return JSONResponse(content=jsonable_encoder(users), status_code=200)

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((user for user in users if user.user_id == user_id), None)
    if user is None:
        return JSONResponse(content={"error": "User not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(user), status_code=200)