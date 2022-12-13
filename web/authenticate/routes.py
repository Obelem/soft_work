
from flask import abort, jsonify, request, render_template
from web import login_manager, login_required, login_user, storage
from models.user import User

from web.authenticate import authenticate_views
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id=None):
    if user_id:
        return storage.check_user(id=user_id)

@authenticate_views.route("/login", methods=["GET", "POST"], strict_slashes=False)
def login():
    # data = request.get_json()

    # if "username" not in data:
    #     return abort(404)

    # if "password" not in data:
    #     return abort(404)

    # user = storage.check_user(data["username"])

    # if not user:
    #     return "Invalid username or password"

    # if check_password_hash(user.password, data["password"]):
    #     login_user(user)
    #     return jsonify("Login successful")

    # return jsonify("Invalid password")

    return render_template("authenticate/login.html")

@authenticate_views.route("/signup", methods=["GET", "POST"], strict_slashes=False)
def signup():
    # data = request.get_json()
    # if "first_name" not in data:
    #     return abort(404)

    # if "last_name" not in data:
    #     return abort(404)

    # if "username" not in data:
    #     return abort(404)

    # if "password" not in data:
    #     return abort(404)

    # if "email" not in data:
    #     return abort(404)

    # data["password"] = generate_password_hash(data["password"])

    # existing_user = storage.check_user(data['username'])
    
    # if existing_user:
    #     return jsonify("Username is not available")

    # user = User(**data)
    # user.save()
    # login_user(user)

    # return jsonify("Account created!")

    return render_template("authenticate/signup.html")


@authenticate_views.route("/logout", methods=["POST"], strict_slashes=False)
def logout():
    pass
