from flask import Flask, jsonify, make_response
from flask_login import LoginManager
from models import storage

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a random string'

login_manager = LoginManager()
login_manager.init_app(app)

from web.views import authenticate_views

app.register_blueprint(authenticate_views)


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
    return make_response(jsonify({'error': "Not found"}), 404)
