from models.storage.db_storage import Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Boolean, Integer
from sqlalchemy.orm import relationship

class Survey(Base):
    __tablename__ = 'survey'
    id = Column('id', Integer, primary_key=True, nullable=False)
    creators_id = Column('creators_id', Integer, ForeignKey('users.id'), nullable=False)
    title = Column('title', String, nullable=False)
    description = Column('description', String, nullable=False)
    form = Column('form', String, nullable=False)
    response = relationship('response', backref='survey', cascade="all, delete, delete-orphan")