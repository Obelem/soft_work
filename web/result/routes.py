#!/usr/bin/python3
from web.result import result_views
from flask import jsonify, abort, request, render_template
from models import storage
from models.question_bank import QuestionBank
from models.assessments import Assessment
from flask_login import login_required, current_user


@result_views.route('/results', methods=['POST'],
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

    total = len(assessment.questions)
    percent_score = round((score / total) * 100, 2)

    setattr(current_user.status, assessment.name, 'done')

    setattr(current_user.score, assessment.name, percent_score)
    storage.save()

    return render_template('result/result.html',
                           total = total,
                           score = score,
                           failed = total - score,
                           percent_score = percent_score,
                        )
