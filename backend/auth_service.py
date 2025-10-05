from auth_functions import create_token , verify_token , verify_password , hashed_password
from schemas import UserRegister, UserLogin, UserInfo, ResponseLogin
from sqlalchemy.orm import Session
from models import User
from fastapi import HTTPException
from typing import List

class AuthService:
    
    def __init__(self , db : Session):
        self.db = db
        
    def register(self , user : UserRegister) -> UserInfo:
        userCheck = self.db.query(User).filter(User.email == user.email).first()
        if userCheck:
            raise HTTPException(
                status_code=400,
                detail="User with this email already exist"
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
        return new_user
    
    
    def login(self , user : UserLogin) -> ResponseLogin:
        userCheck = self.db.query(User).filter(User.email == user.email).first()
        if userCheck is None:
            raise HTTPException(
                status_code=404,
                detail="Unregistered Email"
            )
        
        checkPassword = verify_password(user.password , userCheck.hashed_pass)
        if checkPassword is False:
             raise HTTPException(
                status_code=404,
                detail="Invalid Password"
            )
             
        _token = create_token(user.email)
        token_type = "Bearer"
        
        result = ResponseLogin(
            token = _token,
            token_type = token_type
        )
        return result


    def getUsers(self) -> List[UserInfo]:
        users = self.db.query(User).all()
        return users