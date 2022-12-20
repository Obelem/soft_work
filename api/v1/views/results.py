#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.question_bank import QuestionBank
from models.assessments import Assessment
from flask_login import login_required, current_user


@app_views.route('/results', methods=['POST'],
                strict_slashes=False)
@login_required
def evaluate_results():
    assessments = ['communication_skills', 'listening_skills', 'critical_thinking']
    score = 0

    for assessment in assessments:
        id = request.form.get(assessment)
        if id:
            assessment = storage.get('Assessment', id)
            break

    if not assessment:
        return 'No question'

    for question_bank in assessment.questions:
        answer = request.form.get(question_bank.id)
        if not answer:
            continue
        score += 1 if answer == question_bank.answer else 0

    score = (score / len(assessment.questions)) * 100

    setattr(current_user.status, assessment.name, 'done')
    storage.save()
    return str(round(score, 1)) + '%'



