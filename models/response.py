from models.storage.db_storage import Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Boolean, Integer
from sqlalchemy.orm import relationship

class Response(Base):
    __tablename__ = 'response'
    id = Column('id', Integer, primary_key=True, nullable=False)
    users_id = Column('users_id', Integer, ForeignKey('users.id'), nullable=False)
    survey_id = Column('survey_id', Integer, ForeignKey('survey.id'), nullable=False)
    title = Column('title', String, nullable=False)
    response = Column('response', String, nullable=False)