#!/usr/bin/python3
from models.assessments import Assessment
from models.question_bank import QuestionBank
from models.user import User

# create assessment
assess1 = Assessment(name='listening_skills')
assess2 = Assessment(name='communication_skills')
assess3 = Assessment(name='critical_thinking')

assess1.save()
assess2.save()
assess3.save()


# add questions
listen_question1 = QuestionBank(
    assessment_id = assess1.id,
    assessment_name = 'listening_skills',
    question = 'how many ears do humans have?',
    options=['1', '5', '2'],
    answer='2'
)

listen_question2 = QuestionBank(
    assessment_id = assess1.id,
    assessment_name = 'listening_skills',
    question = 'ear is used for?',
    options=['walking', 'talking', 'hearing'],
    answer='hearing'
)

listen_question3 = QuestionBank(
    assessment_id = assess1.id,
    assessment_name = 'listening_skills',
    question = 'is ear used for balance',
    options=['sometimes', 'no', 'yes'],
    answer='yes'
)

listen_question1.save()
listen_question2.save()
listen_question3.save()


comm_skills1 = QuestionBank(
    assessment_id = assess2.id,
    assessment_name = 'communication_skills',
    question = 'should you hear more or talk more',
    options = ['both', 'hear', 'talk'],
    answer = 'hear'
)


comm_skills1.save()
