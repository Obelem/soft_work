#!/usr/bin/python3
from models.assessments import Assessment
from models.question_bank import QuestionBank
from models.user import User



assess1 = Assessment(name='listening_skills')
assess2 = Assessment(name='communication_skills')
assess3 = Assessment(name='critical_thinking')

assess1.save()
assess2.save()
assess3.save()
