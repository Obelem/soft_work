from .base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.types import JSON
from sqlalchemy.ext.mutable import MutableList


class MarkingScheme(BaseModel, Base):
    __tablename__ = "marking_scheme"

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
