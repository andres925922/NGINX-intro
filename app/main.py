from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os

app = FastAPI()

@app.get("/health")
def health_check():
    return JSONResponse(content={
        "status": "ok",
        "listening_port": os.environ.get("PORT", 8000),
        "app_name": os.environ.get("APP_NAME", "app")
        }, status_code=200)