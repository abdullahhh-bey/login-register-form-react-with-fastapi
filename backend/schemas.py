from pydantic import BaseModel, Field, EmailStr

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
        