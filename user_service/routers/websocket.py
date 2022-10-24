from fastapi import (
    APIRouter,
    WebSocket,
    WebSocketDisconnect,
    Cookie,
)
import os
from jose import jwt
from typing import List
import json
from datetime import datetime, timezone
from routers.accounts import AccountToken
from routers.auth import auth

router = APIRouter()


def timestamp():
    return datetime.now(timezone.utc).isoformat()

# async def get_current_active_user(current_user: AccountToken):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user

class ConnectionManager:
    def __init__(self):
        self.active_connections = dict()
        self.current_message_id = 0

    async def connect(
        self,
        websocket: WebSocket,
    ):
        await websocket.accept()
        token_data = jwt.decode(
            websocket.query_params['token'],
            os.environ["SIGNING_KEY"],
            algorithm="HS256")
        print(token_data)
        username = token_data["username"]
        self.active_connections[username] = websocket
        await self.send_personal_message(
            "Welcome!",
            username,
            websocket,
        )
        return username

    def disconnect(self, username: str):
        del self.active_connections[username] 

    async def send_personal_message(
        self,
        message: str,
        username: str,
        websocket: WebSocket,
    ):
        payload = json.dumps({
            "username": username,
            "content": message,
            "timestamp": timestamp(),
            "message_id": self.next_message_id(),
        })
        await websocket.send_text(payload)

    async def broadcast(self, message: str, username: str):
        payload = json.dumps({
            "username": username,
            "content": message,
            "timestamp": timestamp(),
            "message_id": self.next_message_id(),
        })
        print('active connections:', len(self.active_connections))
        for connection in self.active_connections:
            await connection.send_text(payload)

    def next_message_id(self):
        self.current_message_id += 1
        return self.current_message_id


manager = ConnectionManager()


@router.websocket("/chat")
async def websocket_endpoint(
    websocket: WebSocket
):

    username = await manager.connect(websocket)
    try:
        while True:
            message = await websocket.receive_text()
            await manager.broadcast(message, username)
    except WebSocketDisconnect:
        manager.disconnect(websocket, username)
        await manager.broadcast("Disconnected", username)

