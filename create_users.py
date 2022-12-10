#!/usr/bin/python3
from models.assessments import Assessment
from models.question_bank import QuestionBank
from models.user import User

user1 = User (
    username = 'Johnny90',
    first_name = 'John',
    middle_name = 'Smith',
    last_name = 'Doe',
    email = 'hello@gmail.com',
    password = 'pwd'
)

user2 = User (
    username = 'Tonye90',
    first_name = 'Nimi',
    middle_name = 'Cole',
    last_name = 'Tonye',
    email = 'tonye@gmail.com',
    password = 'pass'
)

user1.save()
user2.save()
