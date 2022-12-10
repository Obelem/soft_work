#!/usr/bin/python3
'''
assessments.py
'''

from .base_model import BaseModel, Base

from sqlalchemy import Column, Integer, String, Text


class Assessment(BaseModel, Base):
    '''
    This class creates an Assesment Object.
    The Assesment object represents a question.
    Attributes of this objects are
        - id: question id
        - question_text: question texts
        - options: options separated by ","
        - answer: correct answer to the question
        - image_url: images that complements a question [optional]
    '''
    __tablename__ = "assessments"

    question_test = Column(Text, nullable=False)
    options = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    image_url = Column(Text)


    def __init__(self, *args, **kwargs):
        '''initialize Assessment Object'''
        super().__init__(*args, **kwargs)
