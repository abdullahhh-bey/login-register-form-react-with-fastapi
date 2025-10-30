# from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
# from chatService import ChatService
# from auth_functions import *
# from connectionmanager import ConnectionManager

# router = APIRouter()

# @router.websocket("/ws/chat/{chat_id}")
# async def websocket_endpoint(
#     websocket: WebSocket,
#     chat_id: int,
#     token: str
# ):
#     """
#     A websocket connection for real-time chatting.
#     """
#     # 1️⃣ Verify user via token
#     user = await get_current_user(token)
#     if not user:
#         await websocket.close(code=1008)  # 1008: policy violation
#         return

#     # 2️⃣ Add this socket to the ConnectionManager
#     await manager.connect(chat_id, websocket)

#     try:
#         # 3️⃣ Listen forever until disconnected
#         while True:
#             data = await websocket.receive_json()

#             # Example of received data:
#             # {
#             #   "content": "hey bro!",
#             #   "owner_id": 1
#             # }

#             # 4️⃣ Save message to DB
#             msg = await ChatService.add_message(
#                 chat_id=chat_id,
#                 owner_id=user["id"],
#                 content=data["content"]
#             )

#             # 5️⃣ Broadcast message to all chat members
#             await manager.broadcast(chat_id, {
#                 "chat_id": chat_id,
#                 "owner_id": user["id"],
#                 "owner_name": user["name"],
#                 "content": data["content"],
#                 "created_at": msg.created_at.isoformat()
#             })

#     except WebSocketDisconnect:
#         # 6️⃣ When user disconnects
#         manager.disconnect(chat_id, websocket)
