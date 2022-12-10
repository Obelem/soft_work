#!/usr/bin/python3
'''

'''

from models.base_model import BaseModel
from models.user import User

base = BaseModel()
print(base)

user = User(first_name='Jeff',
            last_name='Bezos',
            email='hello@gmail.com',
            password='pwd'
            )
user.save()
print(user)
