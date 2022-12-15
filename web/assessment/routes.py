from flask import abort, jsonify, render_template, request, url_for
from web.assessment import assessment_views
from flask_login import login_required, current_user
from models.user import User
from models import storage



@assessment_views.route("/", methods=['GET'])
@login_required
def assessment_page():
    return render_template(
        "assessment/assessment.html",
    )
