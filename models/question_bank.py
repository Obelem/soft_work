from .base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Integer
from sqlalchemy.types import JSON
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship


class QuestionBank(BaseModel, Base):
    __tablename__ = "question_bank"

    assessment_name = Column(String(60), nullable=False)

    assessment_id = Column(
        String(60),
        ForeignKey('assessments.id'),
        nullable=False
    )

    question = Column(Text, nullable=False)

    options = Column(
        MutableList.as_mutable(JSON),
        nullable=False,
        default=[]
    )

    answer = Column(Text, nullable=False)
    image_url = Column(Text)

    assessment = relationship('Assessment', back_populates='questions')
