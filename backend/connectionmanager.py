from typing import Dict, Set
from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[int, Set[WebSocket]] = {}

    async def connect(self, chat_id: int, websocket: WebSocket):
        await websocket.accept()
        if chat_id not in self.active_connections:
            self.active_connections[chat_id] = set()
        self.active_connections[chat_id].add(websocket)

    def disconnect(self, chat_id: int, websocket: WebSocket):
        if chat_id in self.active_connections:
            self.active_connections[chat_id].discard(websocket)
            if not self.active_connections[chat_id]:
                del self.active_connections[chat_id]

    async def broadcast(self, chat_id: int, message: dict):
        """Send a JSON message to all sockets in a chat."""
        if chat_id in self.active_connections:
            dead_connections = []
            for connection in self.active_connections[chat_id]:
                try:
                    await connection.send_json(message)
                except Exception:
                    dead_connections.append(connection)
            # Cleanup any broken sockets
            for dc in dead_connections:
                self.disconnect(chat_id, dc)
