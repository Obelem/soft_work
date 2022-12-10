#!/usr/bin/python3
'''

'''

from models.base_model import BaseModel
from models.user import User
from models.assessments import Assessment

base = BaseModel()
print(base)

# user = User(
#             username='JBez',
#             first_name='Jeff',
#             last_name='Bezos',
#             email='hello@gmail.com',
#             password='pwd'
#             )
# user.save()
# print(user)

assessment = Assessment(
    question_test='how are you?',
    options='nice, just there',
    answer='fine'
)
assessment.save()
print(assessment)

