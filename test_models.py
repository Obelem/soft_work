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

options = ['Europe', 'Asia', 'Africa']
assessment = Assessment(
    question_test='What continent is Nigeria in?',
    options=options,
    answer='Africa'
)
assessment.save()
print(assessment.options)

