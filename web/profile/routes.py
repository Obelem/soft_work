from flask import abort, jsonify, render_template, request, url_for
from web.profile import profile_views
from flask_login import login_required, current_user



@profile_views.route("/", methods=['GET'])
@login_required
def profile_page():
    return render_template("profile/profile.html")
