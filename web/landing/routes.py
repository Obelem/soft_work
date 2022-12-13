from flask import abort, jsonify, render_template, request, url_for
from web.landing import landing_views


@landing_views.route("/", methods=['GET'], strict_slashes=False)
def landing_page():
    return render_template("landing/index.html")

