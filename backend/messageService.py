from schemas import *
from fastapi import HTTPException
from models import *
from sqlalchemy.orm import Session

class MessageService():
    def __init__(self, db : Session):
        self.db = db
        
    def sendMessage(self, data : AddMessage) -> ResponseMessage:
        chat = self.db.query(Chat).filter(Chat.id == data.chat_id).first()
        if chat is None:
            raise HTTPException(
                status_code=404,
                detail="Chat dont exists"
            )
        
        user = self.db.query(User).filter(User.id == data.owner_id).first()
        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User dont exists"
            )
        
        message = Message(
            content = data.content,
            owner_id = data.owner_id,
            chat_id = data.chat_id
        )
        
        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)
        
        return message
            