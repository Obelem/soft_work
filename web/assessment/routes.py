from flask import abort, jsonify, render_template, request, url_for
from web.assessment import assessment_views
from flask_login import login_required, current_user
from models import storage



@assessment_views.route("/<assessment_name>", methods=['GET'])
@login_required
def assessment_page(assessment_name):
    assessments = storage.all('Assessment').values()
    for assessment in assessments:
        if assessment.name == assessment_name:
            current_assessment = assessment
            break

    return render_template(
        "assessment/assessment.html",
        current_assessment = current_assessment
    )
