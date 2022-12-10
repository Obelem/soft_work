#!/usr/bin/python3
'''test user assessment'''
from models.base_model import BaseModel
from models.user import User
from models.assessments import Assessment
from models.marking_scheme import MarkingScheme

user1 = User(
    username = 'new_user',
    first_name = 'Jimmy',
    middle_name = 'Pepple',
    last_name = 'Tonye',
    email = 'hello@gmail.com',
    password = 'pwd'
)

user1.save()

assess1 = Assessment(
    name = 'critical_thinking',
    user_id = user1.id,
)

assess2 = Assessment(
    name = 'listening_skills',
    user_id = user1.id
)

assess1.save()
assess2.save()

[print(assess) for assess in user1.assessments]


print('ok')
