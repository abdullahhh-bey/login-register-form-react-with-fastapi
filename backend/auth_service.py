from auth_functions import *
from schemas import UserRegister, UserLogin, UserInfo, ResponseLogin, ResetPassRequest
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
    
    def forgotPassword(self, email : str) -> str:
        user = self.db.query(User).filter(User.email == email).first()
        if user is None:
            raise HTTPException(
                status_code=404,
                detail="No User with this email"
            )  
        
        reset_token = create_reset_token(str(user.id) , user.email)
        return reset_token
        
        
    def resetPassword(self, res : ResetPassRequest) -> str:
        id = verify_reset_token(res.token)
        
        if id is None:
            raise HTTPException(
                status_code=400,
                detail="Invalid token!!!"
            )
            
        user = self.db.query(User).filter(User.id == int(id)).first()
        new_hash_pass = hashed_password(res.new_password)
        user.hashed_pass = new_hash_pass
        self.db.commit()
        return "Password has been changed"