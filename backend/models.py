from database import Base, engine
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base, sessionmaker


class User(Base):
    
    __tablename__ = "users"

    id = Column(Integer , primary_key=True, index=True)
    name = Column(String , nullable=False)
    email = Column(String(255),index=True , nullable=False, unique=True)
    hashed_pass = Column(String, nullable=False)
    is_verified = Column(Boolean , default=False)

    sent_contacts = relationship(
        "Contact",
        foreign_keys="Contact.user_id",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    
    received_contacts = relationship(
        "Contact",
        foreign_keys="Contact.friend_id",
        back_populates="friend",
        cascade="all, delete-orphan"
    )
    
    def following(self):
        
        

class Contact(Base):
    __tablename__ = "contacts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"),index=True)
    friend_id = Column(Integer, ForeignKey("users.id"), index=True)
    
    __table_args__ = (UniqueConstraint("user_id", "friend_id", name="uq_user_friend"),)

    user = relationship("User", foreign_keys=[user_id], back_populates="sent_contacts")
    friend = relationship("User", foreign_keys=[friend_id], back_populates="received_contacts")
    

Base.metadata.create_all(bind=engine)

