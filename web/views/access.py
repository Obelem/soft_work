
from flask import abort, jsonify, request
from flask_login import login_required, login_user

from models import storage
from models.user import User

from web.views import authenticate_views
from web import login_manager, storage
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id=None):
    if user_id is not None:
        pass

@authenticate_views.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if "username" not in data:
        return abort(404)

    if "password" not in data:
        return abort(404)

    user = storage.check_user(data["username"])

    if not user:
        return "Invalid username or password"

    if check_password_hash(user.password, data["password"]):
        login_user(user)
        return jsonify("Login successful")

    return jsonify("Invalid password")

@authenticate_views.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    if "first_name" not in data:
        return abort(404)

    if "last_name" not in data:
        return abort(404)

    if "username" not in data:
        return abort(404)

    if "password" not in data:
        return abort(404)

    if "email" not in data:
        return abort(404)

    data["password"] = generate_password_hash(data["password"])

    existing_user = storage.check_user(data['username'])
    
    if existing_user:
        return jsonify("Username is not available")

    user = User(**data)
    user.save()
    login_user(user)

    return jsonify("Account created!")


@authenticate_views.route("/logout", methods=["POST"])
def logout():
    pass
