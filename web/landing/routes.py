from flask import abort, jsonify, render_template, request, url_for
from flask_login import current_user
from web.landing import landing_views


@landing_views.route("/", methods=['GET'])
@landing_views.route("/welcome/", methods=['GET'])
def landing_page():
    return render_template("landing/index.html", current_user=current_user)

