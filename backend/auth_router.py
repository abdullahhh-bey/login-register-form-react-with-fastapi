from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas import UserInfo , UserRegister, UserLogin, ResponseLogin, ResetPassRequest
from database import get_db
from auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Login & Register"]
)

@router.get("/users", response_model=List[UserInfo])
def GetUsers(db : Session = Depends(get_db)) -> List[UserInfo]:
    service = AuthService(db)
    u = service.getUsers()
    return u


@router.post("/register" , response_model=UserInfo)
def RegisterUser( u : UserRegister , db : Session = Depends(get_db)) -> UserInfo:
    service = AuthService(db)
    u = service.register(u)
    return u


@router.post("/login" , response_model=ResponseLogin)
def LoginUser(u : UserLogin , db : Session = Depends(get_db)) -> ResponseLogin:
    service = AuthService(db)
    t = service.login(u)
    return t


@router.post("/forgot-password")
def ForgotPassword( email : str ,db : Session = Depends(get_db)) -> str:
    service  = AuthService(db)
    reset_token = service.forgotPassword(email)
    return reset_token


@router.post("/new_password")
def newPassword(res : ResetPassRequest, db : Session = Depends(get_db)) -> str:
    service = AuthService(db)
    response = service.resetPassword(res)
    return response