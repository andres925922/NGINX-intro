from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/auth')
async def auth(request: Request):
    auth_header = request.headers.get('Authorization')
    if auth_header is None or not auth_header.startswith('Bearer '):
        return JSONResponse(status_code=401, content={'error': 'Missing or invalid Authorization header'})
    
    token = auth_header.split(' ')[1]

    # Check if token is valid
    if token != 'valid_token':
        return JSONResponse(status_code=401, content={'error': 'Invalid token'})
    
    return JSONResponse(status_code=200, content={'message': 'Token is valid'})