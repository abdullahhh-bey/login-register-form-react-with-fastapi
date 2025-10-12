from sqlalchemy.orm import Session
from models import User, Contact
from fastapi import HTTPException, status
from schemas import AddContactDTO,UserInfo


def add_contact(db: Session, req : AddContactDTO):
    user = db.query(User).filter(User.email == req.user_email).first()
    friend = db.query(User).filter(User.email == req.friend_email).first()

    if not user or not friend:
        raise HTTPException(status_code=404, detail="User not found")

    if user.id == friend.id:
        raise HTTPException(status_code=400, detail="Cannot add yourself")

    existing = db.query(Contact).filter(
        ((Contact.user_id == user.id) & (Contact.friend_id == friend.id)) |
        ((Contact.user_id == friend.id) & (Contact.friend_id == user.id))
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Already connected")

    contact = Contact(user_id=user.id, friend_id=friend.id)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return {"message": f"{friend.name} added as FRIEND for {user.name}"}


def get_contacts(db: Session, user_email: str):
    user = db.query(User).filter(User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    users = user.all_friends()
    
    u = [UserInfo(
        name = u.name,
        id = u.id,
        email = u.email
    ) for u in users]
    
    return u