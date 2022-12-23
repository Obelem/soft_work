from flask import abort, jsonify, render_template, request, url_for
from web.profile import profile_views
from flask_login import login_required, current_user
from models.user import User
from models import storage



@profile_views.route("/", methods=['GET'])
@login_required
def profile_page():
    return render_template(
        "profile/profile.html",
        first_name=current_user.first_name,
        last_name=current_user.last_name,
        middle_name=current_user.middle_name,
        username = current_user.username,
        status = current_user.status,
        assessments = storage.all('Assessment').values(),
        score = current_user.score
    )
