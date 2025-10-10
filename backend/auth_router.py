from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas import UserInfo , UserRegister, UserLogin, ResponseLogin, ResetPassRequest, ForgotPasswordDto
from database import get_db
from auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Login & Register"]
)

#dependency provider
def get_authSerivce(db : Session = Depends(get_db)):
    return AuthService(db)


@router.get("/users", response_model=List[UserInfo])
def GetUsers(service : AuthService = Depends(get_authSerivce) ,db : Session = Depends(get_db)) -> List[UserInfo]:
    u = service.getUsers()
    return u


@router.post("/register")
async def RegisterUser(u : UserRegister ,service : AuthService = Depends(get_authSerivce) , db : Session = Depends(get_db)) -> str:
    u = await service.register(u)
    return u


@router.post("/login" , response_model=ResponseLogin)
def LoginUser( u : UserLogin , service : AuthService = Depends(get_authSerivce), db : Session = Depends(get_db)) -> ResponseLogin:
    t = service.login(u)
    return t



@router.post("/forgot-password")
def ForgotPassword( forget : ForgotPasswordDto, service : AuthService = Depends(get_authSerivce) ,db : Session = Depends(get_db)) -> str:
    reset_token = service.forgotPassword(forget.email)
    return reset_token


@router.post("/new-password")
def newPassword(res : ResetPassRequest, service : AuthService = Depends(get_authSerivce) , db : Session = Depends(get_db)) -> str:
    response = service.resetPassword(res)
    return response


@router.post("/verify-email")
def verifyEmail(token : str, service : AuthService = Depends(get_authSerivce) , db : Session = Depends(get_db)):
    res = service.email_verification(token)
    return res