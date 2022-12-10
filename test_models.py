#!/usr/bin/python3
'''

'''

from models.base_model import BaseModel
from models.user import User
from models.assessments import Assessment
from models.marking_scheme import MarkingScheme

# base = BaseModel()
# print(base)

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

assessment = Assessment(name='Critical Thinking')
assessment.save()

marking_scheme = MarkingScheme(
    assessment_id=assessment.id,
    question='which continent is Nigeria found?',
    options=options,
    answer='Africa'
)

marking_scheme.save()

print(assessment.id)
print(marking_scheme.assessment_id)
print(marking_scheme.options)
print(marking_scheme.options[0])

print('making changes')

marking_scheme.options[0] = 'Australia'
marking_scheme.save()

print(marking_scheme.options[0])

