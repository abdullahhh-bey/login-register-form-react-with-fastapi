from database import Base, engine
from sqlalchemy import Column, Integer, String, Boolean

class User(Base):
    
    __tablename__ = "users"

    id = Column(Integer , primary_key=True, index=True)
    name = Column(String , nullable=False)
    email = Column(String(255),index=True , nullable=False, unique=True)
    hashed_pass = Column(String, nullable=False)
    is_verified = Column(Boolean , default=False)

Base.metadata.create_all(bind=engine)

