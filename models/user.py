from models.storage.db_storage import Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Boolean, Integer
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, nullable=False)
    email = Column('email', String, nullable=False)
    password = Column('password', String, nullable=False)
    creator = Column('creator', Boolean, default=False)