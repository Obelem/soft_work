'''user.py'''
from .base_model import BaseModel, Base
from sqlalchemy import Boolean, Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship


class Status(BaseModel, Base):
    '''stores assessment status of user'''
    __tablename__ = 'status'

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    listening_skills = Column(String(60))
    communication_skills = Column(String(60))
    critical_thinking = Column(String(60))

    user = relationship('User', back_populates='status')
