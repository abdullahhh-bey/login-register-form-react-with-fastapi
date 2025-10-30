from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas import *
from database import get_db
from messageService import MessageService


MessageRouter = APIRouter(
    prefix="/chats/messages",
    tags=["Messages"]
)



def getMessageService(db : Session = Depends(get_db)):
    return MessageService(db)


@MessageRouter.post("/")
def sendMessageAPI(data : AddMessage , service : MessageService = Depends(getMessageService)):
    res = service.sendMessage(data)
    return res

@MessageRouter.get("/")
def getMessagesAPI(chat_id : int , service : MessageService = Depends(getMessageService)):
    res = service.getMessages(chat_id)
    return res
