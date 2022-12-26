from flask import abort, jsonify, render_template, request, url_for
from web.profile import profile_views
from flask_login import login_required, current_user
from models.user import User
from models import storage

from web.tools.certificates1 import get_aws_s3_link



@profile_views.route("/", methods=['GET'])
@login_required
def profile_page():
    if not current_user.profile_pic:
        link = get_aws_s3_link("default", "dps")
    else:
        link = get_aws_s3_link(current_user.username, "dps")
        current_user.profile_pic = link
        storage.save()
    print(link)
    return render_template(
        "profile/profile.html",
        first_name=current_user.first_name,
        last_name=current_user.last_name,
        middle_name=current_user.middle_name,
        username = current_user.username,
        status = current_user.status,
        assessments = storage.all('Assessment').values(),
        score = current_user.score,
        user_id = current_user.id,
        profile_pic = link
    )
