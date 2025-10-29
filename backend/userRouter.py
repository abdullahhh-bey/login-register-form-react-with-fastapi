from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas import UserInfo , UserRegister, UserLogin, ResponseLogin, ResetPassRequest, ForgotPasswordDto, AddContactDTO
from database import get_db
from userService import *

UserRouter = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@UserRouter.get("/")
def getUserByEmail( email : str, db : Session = Depends(get_db)):
    user = get_user_by_email(db, email)
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="No user found"
        )
    return {
        "name" :  user.name,
        "id" : user.id,
        "email" : user.email,
        "verified" : user.is_verified
    }


# add the dto in response of the above endpoint
#create endpoints for contacts

