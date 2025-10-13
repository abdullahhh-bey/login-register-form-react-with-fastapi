from fastapi import HTTPException
from models import *
from schemas import * 
from sqlalchemy.orm import Session
from datetime import datetime

class ChatService:
    
    def __init__(self, db : Session):
        self.db = db
        
    def addChat(self, chat : AddChatInfo):
        
        
    