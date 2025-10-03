from auth_functions import create_token , verify_token , verify_password , hashed_password
from schemas import UserRegister, UserLogin, UserInfo
from sqlalchemy.orm import Session
from models import User
from fastapi import HTTPException

class AuthService:
    
    def __init__(self , db : Session):
        self.db = db
        
    def register(self , user : UserRegister) -> UserInfo:
        userCheck = self.db.query(User).filter(User.email == user.email).first()
        if userCheck:
            raise HTTPException(
                status_code=400,
                detail="User with this Id already exist"
            )
            
        _pass = hashed_password(user.password)
        new_user = User(
            name = user.name,
            email = user.email,
            hashed_pass = _pass
        )
        
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return UserInfo
    
    def 