from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import datetime

class UserRegister(BaseModel):
    
    name : str = Field(...)
    email : EmailStr = Field(...)
    password : str = Field(..., min_length=8, max_length=30)
    
class UserLogin(BaseModel):
    
    email : EmailStr = Field(...)
    password : str = Field(...,  min_length=8, max_length=30)
     
     
class ResponseLogin(BaseModel):
    
    token : str
    token_type : str
    
class UserInfo(BaseModel):
    id : int
    name : str
    email : EmailStr 
   
    class Config:
        orm_mode = True
        
        
class ResetPassRequest(BaseModel):
    new_password : str
    token : str
    
    class Config:
        orm_mode = True
        
class ForgotPasswordDto(BaseModel):
    email : str
    
    class Config:
        orm_mode = True
        
        
class AddContactDTO(BaseModel):
    user_email : str = Field(...)
    friend_email : str = Field(...)
    
 
class AddChatInfo(BaseModel):
    is_group: bool = Field(..., description="True if group chat, False for private chat")
    name: str | None = Field(None, description="Name for group chat; optional for private chat")
    user_email: List[EmailStr] = Field(..., description="List of user emails to include in the chat")


class ChatWithUsers(BaseModel):
    id: int
    is_group: bool
    group_name: str | None
    users: List[str]
    group_created_at: datetime

    class Config:
        orm_mode = True
        
        
class ChatInfo(BaseModel):
    id : int
    Is_group : bool
    Chat_name : str
    created_at : datetime
    
    class Config:
        orm_mode = True
        