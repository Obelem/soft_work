from flask import Flask
from flask_login import LoginManager
from models import storage

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a random string'

login_manager = LoginManager()
login_manager.init_app(app)

from web.views import authenticate_views

app.register_blueprint(authenticate_views)
