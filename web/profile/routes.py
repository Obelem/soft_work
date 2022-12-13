from flask import abort, jsonify, render_template, request, url_for
from web.profile import profile_views
from web import login_required

@login_required
@profile_views.route("/", methods=['GET'], strict_slashes=False)
def profile_page():
    return render_template("profile/profile.html")
