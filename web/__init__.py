from flask import Flask, jsonify, make_response, render_template
from flask_login import LoginManager, login_user, logout_user
from models import storage

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a random string'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return storage.check_user(user_id)

from web.authenticate import authenticate_views
from web.landing import landing_views
from web.profile import profile_views

app.register_blueprint(authenticate_views)
app.register_blueprint(landing_views)
app.register_blueprint(profile_views, url_prefix="/profile")


login_manager.login_view = "authenticate_views.login"


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return render_template("404.html")

