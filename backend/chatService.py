from fastapi import HTTPException
from models import *
from schemas import * 
from sqlalchemy.orm import Session
from datetime import datetime

class ChatService:
    
    def __init__(self, db : Session):
        self.db = db
        
 
    def create_chat(self, chat_data: AddChatInfo) -> ChatWithUsers:
        if not chat_data.user_email or len(chat_data.user_email) == 0:
            raise HTTPException(
                status_code=400, 
                detail="At least one user must be provided"
            )

        users = self.db.query(User).filter(User.email.in_(chat_data.user_email)).all()
        if len(users) != len(chat_data.user_email):
            found_emails = [u.email for u in users]
            missing = list(set(chat_data.user_email) - set(found_emails))
            raise HTTPException(status_code=404, detail=f"Users not found: {missing}")


        if chat_data.is_group:
            if not chat_data.name:
                raise HTTPException(status_code=400, detail="Group chat must have a name")
        else:
            if len(users) != 2:
                raise HTTPException(status_code=400, detail="Private chat must have exactly 2 users")

        chat = Chat(Chat_name=chat_data.name, Is_group=chat_data.is_group)
        self.db.add(chat)
        self.db.commit()
        self.db.refresh(chat)

        for user in users:
            member = ChatMember(chat_id=chat.id, user_id=user.id)
            self.db.add(member)
        self.db.commit()

        return ChatWithUsers(
            id=chat.id,
            is_group=chat.Is_group,
            group_name=chat.Chat_name,
            users=[u.email for u in users],
            group_created_at=chat.created_at,
        )



            
    def get_user_all_chats(self,user_email: str):
        user = self.db.query(User).filter(User.email == user_email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        chats = (
            self.db.query(Chat)
            .join(ChatMember)
            .filter(ChatMember.user_id == user.id)
            .all()
        )

        return [
            ChatWithUsers(
                id=c.id,
                is_group=c.Is_group,
                group_name=c.Chat_name,
                users=[m.user.email for m in c.members],
                group_created_at=c.created_at,
            )
            for c in chats
        ]


    def add_user_in_chat(self, data : AddUserInChat):
        chat = self.db.query(Chat).filter(Chat.id == data.chat_id).first()
        if chat is None:
            raise HTTPException(
                status_code=404,
                detail="Chat dont exist"
            )
            
        if chat.Is_group is False:
            raise HTTPException(
                status_code=400,
                detail="Private chat can only have 2 members"
            )
        
        users = self.db.query(User).filter(User.email.in_(data.user_email)).all()
        if len(users) != len(data.user_email):
            found_emails = [u.email for u in users]
            missing = list(set(data.user_email) - set(found_emails))
            raise HTTPException(status_code=404, detail=f"Users not found: {missing}")

        existing_members = self.db.query(ChatMember).filter(ChatMember.chat_id == data.chat_id).all()
        existing_user_ids = {m.user_id for m in existing_members}

        new_users = [u for u in users if u.id not in existing_user_ids]
        #EXISTING USERS
        existing_users = [u for u in users if u.id in existing_user_ids]

        for user in new_users:
            self.db.add(ChatMember(chat_id=data.chat_id, user_id=user.id))

        self.db.commit()
        return f"Users added in the {chat.Chat_name} Group"
