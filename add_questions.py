#!/usr/bin/python3
from models.assessments import Assessment
from models.question_bank import QuestionBank
from models.user import User

# create assessment objects
listening_skills = Assessment(name='Listening Skills')
communication_skills = Assessment(name='Communication Skills')
critical_thinking = Assessment(name='Critical Thinking')

# save assessments
listening_skills.save()
communication_skills.save()
critical_thinking.save()


# add Listening Skills questions
listen_1 = QuestionBank(
    assessment_id = listening_skills.id,
    assessment_name = listening_skills.name,
    question = "A teacher reads the passage and asks questions to the students.\
                (The students don't have the text with them.\
                The teacher is trying to improve the students",
    options=[
        'writing skills',
        'reading skills',
        'listening skills',
        'speaking skills'
    ],
    answer='listening skills'
)

listen_2 = QuestionBank(
    assessment_id = listening_skills.id,
    assessment_name = listening_skills.name,
    question = 'Paying attention to a certain piece of information in a part of listening text, is known as',
    options=[
        'Creative Listening',
        'Selective Listening',
        'Critical Listening',
        'Appreciative Listening'
    ],
    answer='Selective Listening'
)

listen_3 = QuestionBank(
    assessment_id = listening_skills.id,
    assessment_name = listening_skills.name,
    question = 'A teacher provides a theme or a situation for the students to discuss after they have heard a story, read a passage or a news item. What is this listening known as?',
    options=[
        'Extensive Listening',
        'Attentive Listening',
        'Intensive Listening',
        'Responsive Listening'
    ],
    answer='Responsive Listening'
)

listen_4 = QuestionBank(
    assessment_id = listening_skills.id,
    assessment_name = listening_skills.name,
    question = 'Which skill is the basis of good learning of the language?',
    options=[
        'Speaking skill',
        'Explaining skill',
        'Reinforcement skill',
        'Listening skill'
    ],
    answer='Listening skill'
)

listen_5 = QuestionBank(
    assessment_id = listening_skills.id,
    assessment_name = listening_skills.name,
    question = 'The exercise of listening skill is',
    options=[
        'Sports commentary on a radio',
        'Advertisement board',
        'Pamphlet',
        'Poster'
    ],
    answer='Sports commentary on a radio'
)

listen_6 = QuestionBank(
    assessment_id = listening_skills.id,
    assessment_name = listening_skills.name,
    question = 'Transactional listening',
    options=[
        'lays emphasis on conveying information.',
        'lays emphasis on harmonious communication in the social context.',
        'does not require careful attention to details and facts.',
        'is interactive by nature.'
    ],
    answer='lays emphasis on conveying information.'
)

listen_7 = QuestionBank(
    assessment_id = listening_skills.id,
    assessment_name = listening_skills.name,
    question = 'A teacher arranges her learners into pairs and give them a text of two paragraphs. \
                One learner in the pair reads out the text to the other and the partner takes the dictation. \
                Then the process is reversed. What is this known as?',
    options=[
        'Running dictation',
        'Composition dictation',
        'Jig-saw dictation',
        'Partial dictation'
    ],
    answer='Composition dictation'
)

listen_8 = QuestionBank(
    assessment_id = listening_skills.id,
    assessment_name = listening_skills.name,
    question = 'Which of the following activities is used with painting?',
    options=[
        'Listen and label',
        'Listen and guess',
        'Listen and predict',
        'Listen and repeat'
    ],
    answer='Listen and guess'
)




# save questions
listen_1.save()
listen_2.save()
listen_3.save()
listen_4.save()
listen_5.save()
listen_6.save()
listen_7.save()
listen_8.save()


# add communication skills questions
comm_skills_1 = QuestionBank(
    assessment_id = communication_skills.id,
    assessment_name = communication_skills.name,
    question = '___ are the essential component of interpersonal communication.',
    options = [
        'Intrapersonal relationships',
        'Hostile relationships',
        'Interpersonal relationships',
        'lack of refinement'
    ],
    answer = 'Interpersonal relationships'
)

comm_skills_2 = QuestionBank(
    assessment_id = communication_skills.id,
    assessment_name = communication_skills.name,
    question = 'Transactional communication is a ____ process created by the participants through their interaction with each other.',
    options = [
        'Dynamic',
        'Lethargic',
        'Complex ',
        'Simple'
    ],
    answer = 'Dynamic'
)

comm_skills_3 = QuestionBank(
    assessment_id = communication_skills.id,
    assessment_name = communication_skills.name,
    question = 'The quality of interaction in a given situation may be enhanced or hampered by variables such as Complementarity, Divergence, Convergence, and ______.',
    options = [
        'Compensation',
        'Incompatible',
        'Hindrance',
        'Contrary'
    ],
    answer = 'Compensation'
)


# save questions
comm_skills_1.save()
comm_skills_2.save()
comm_skills_3.save()



# add critical thinking questions
critical_thinking_1 = QuestionBank(
    assessment_id = critical_thinking.id,
    assessment_name = critical_thinking.name,
    question = 'A self-guided, self-disciplined thinking which attempts to reason at the highest level of quality in a fair-minded way is called—',
    options = [
        'critical thinking',
        'complex thinking',
        'intelligent thinking',
        'abstract thinking'
    ],
    answer = 'critical thinking'
)

critical_thinking_2 = QuestionBank(
    assessment_id = critical_thinking.id,
    assessment_name = critical_thinking.name,
    question = 'Why should students learn to be critical?',
    options = [
        'To print out flaws and being cynical about everything.',
        'To maintain the status quo in society.',
        'To understand how issues are related to their own lives.',
        'To appreciate uniform, homogeneous perspective.'
    ],
    answer = 'To understand how issues are related to their own lives.'
)


critical_thinking_2 = QuestionBank(
    assessment_id = critical_thinking.id,
    assessment_name = critical_thinking.name,
    question = 'What is the testing objective of the question given within brackets?\n\
                (What will be the time difference between two successive spring tides if the moon takes 30 days to revolve around the earth?)',
    options = [
        'Recall based',
        'Recognition based',
        'Understanding',
        'Skill based'
    ],
    answer = 'Understanding'
)

# save questions
critical_thinking_1.save()
critical_thinking_2.save()
