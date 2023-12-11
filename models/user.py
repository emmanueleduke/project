import models
from hashlib import md5
from models.base import Base, BaseModel
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    __tablename__ = 'users'
    email = Column('email', String(60), nullable=False, unique=True)
    password = Column('password', String(60), nullable=False)
    creator = Column('creator', Boolean, default=False)
    session_id = Column('session_id', String(250), nullable=True)
    reser_token = Column('reser_token', String(250), nullable=True)

    def __init__(self, **kwargs):
        """Create the instance"""
        super().__init__(**kwargs)

    def __setattr__(self, __name, __value):
        if __name == "password":
            __value = md5(__value.encode()).hexdigest()
        super().__setattr__(__name, __value)
