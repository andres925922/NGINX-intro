from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse

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