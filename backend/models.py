from database import Base, engine
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, UniqueConstraint, DateTime
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from datetime import datetime, time

class User(Base):
    
    __tablename__ = "users"

    id = Column(Integer , primary_key=True, index=True)
    name = Column(String , nullable=False)
    email = Column(String(255),index=True , nullable=False, unique=True)
    hashed_pass = Column(String, nullable=False)
    is_verified = Column(Boolean , default=False)
    created_at = Column(DateTime, default=datetime.utcnow)


    chat_memberships = relationship("ChatMember", back_populates="user", cascade="all, delete-orphan")
    messages_sent = relationship("Message", back_populates="owner", cascade="all, delete-orphan")


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
        sent = [c.friend for c in self.sent_contacts]
        print(sent)
        return sent
    
    def followers(self):
        friends = [c.user for c in self.received_contacts]
        print(friends)
        return friends
    
    def all_friends(self):
        return self.followers() + self.following() 
    

class Contact(Base):
    __tablename__ = "contacts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"),index=True)
    friend_id = Column(Integer, ForeignKey("users.id"), index=True)
    
    __table_args__ = (UniqueConstraint("user_id", "friend_id", name="uq_user_friend"),)

    user = relationship("User", foreign_keys=[user_id], back_populates="sent_contacts")
    friend = relationship("User", foreign_keys=[friend_id], back_populates="received_contacts")
    
    
    
class Chat(Base):
    
    __tablename__= "chats"
    
    id = Column(Integer, primary_key=True, index=True)
    Is_group = Column(Boolean, nullable=True, default=False)
    Chat_name = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    members = relationship("ChatMember", back_populates="chat", cascade="all, delete-orphan")
    messages = relationship("Message", back_populates="chat", cascade="all, delete-orphan")

    
class Message(Base):
    
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    chat_id = Column(Integer, ForeignKey("chats.id") ,nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    chat = relationship("Chat", back_populates="messages")
    owner = relationship("User", back_populates="messages_sent")


class ChatMember(Base):
    
    __tablename__ = "chat_members"
    
    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, ForeignKey("chats.id", ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    chat = relationship("Chat", back_populates="members")
    user = relationship("User", back_populates="chat_memberships")

Base.metadata.create_all(bind=engine)

