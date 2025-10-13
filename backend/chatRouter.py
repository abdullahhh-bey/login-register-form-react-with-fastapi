from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas import AddChatInfo,  ChatInfo, ChatWithUsers
from database import get_db
from chatService import ChatService


ChatRouter = APIRouter(
    prefix="/chats",
    tags=["Chats"]
)


#dependency provider
def getChatService(db : Session = Depends(get_db)):
    return ChatService(db)


@ChatRouter.post("/")
def addChatsAPI(chat : AddChatInfo, service : ChatService = Depends(getChatService)):
    chat = service.create_chat(chat)
    return chat


@ChatRouter.get("/")
def getChatsAPI( user_email : str , service : ChatService = Depends(getChatService)):
    user_chats = service.get_user_all_chats(user_email)
    return user_chats