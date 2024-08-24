from fastapi import Depends, FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer

from opendevin.logger import opendevin_logger as logger
from opendevin.server.auth import get_sid_from_token, sign_token

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3001'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

security_scheme = HTTPBearer()

@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    sid = get_sid_from_token(websocket.query_params.get('token') or '')
    if sid == '':
        logger.error('Failed to decode token')
        return 
    
    