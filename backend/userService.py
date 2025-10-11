from sqlalchemy.orm import Session
from models import User

def get_user_by_email(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    return user

def get_all_users(db: Session):
    return db.query(User).all()
