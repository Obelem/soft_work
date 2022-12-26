from flask import abort, jsonify, render_template, request, url_for, abort, redirect
from web.assessment import assessment_views
from flask_login import login_required, current_user
from models import storage
from models.question_bank import QuestionBank
from models.assessments import Assessment



@assessment_views.route("/<assessment_name>", methods=['GET', 'POST'],
                        strict_slashes=False)
@login_required
def assessment_page(assessment_name):
    if request.method == 'GET':
        if getattr(current_user.status, assessment_name):
            return redirect(url_for('profile_views.profile_page'))

        assessments = storage.all('Assessment').values()
        for assessment in assessments:
            if assessment.name == assessment_name:
                current_assessment = assessment
                break

        return render_template(
            "assessment/assessment.html",
            current_assessment = current_assessment
        )

    if request.method == 'POST':
        if request.headers.get('Content-Type') != 'application/json':
            abort(400, description='Not a JSON')

        assessments = ['communication_skills', 'listening_skills', 'critical_thinking']
        score = 0

        request_data = request.get_json()

        for assessment in assessments:
            id = request_data.get(assessment)
            if id:
                assessment = storage.get('Assessment', id)
                break

        if not assessment:
            abort(404)

        correct_answers = {}

        for question_bank in assessment.questions:
            answer = request_data.get(question_bank.id)
            if not answer:
                correct_answers[question_bank.id] = question_bank.answer
                continue
            score += 1 if answer == question_bank.answer else 0
            correct_answers[question_bank.id] = question_bank.answer

        total = len(assessment.questions)
        percent_score = round((score / total) * 100, 2)

        setattr(current_user.status, assessment.name, 'done')

        setattr(current_user.score, assessment.name, percent_score)

        storage.save()

        report_card = {
            'score': score,
            'total': total,
            'failed': total - score,
            'percent_score' : percent_score
        }

        return jsonify([report_card, correct_answers])
