from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas import  ResponseLogin, ResetPassRequest, ForgotPasswordDto, AddContactDTO
from database import get_db
from contactService import *

ContactRouter = APIRouter(
    prefix="/contacts",
    tags=["Contacts"]
)


@ContactRouter.post("/")
def AddContact(contact : AddContactDTO, db : Session = Depends(get_db)):
    result = add_contact(db, contact)
    return result

@ContactRouter.get("/")
def GetFriendsByUser(email : str, db : Session = Depends(get_db)):
    result = get_contacts(db, email)
    return result   