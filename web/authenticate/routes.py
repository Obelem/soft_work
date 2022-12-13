
from flask import abort, jsonify, redirect, request, render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user
from web import storage, login_manager
from models.user import User

from web.authenticate import authenticate_views
from werkzeug.security import generate_password_hash, check_password_hash


@authenticate_views.route("/login", methods=["GET", "POST"], strict_slashes=False)
def login():
    if request.method == "POST":
        username = request.form.get("username", None)
        password = request.form.get("password", None)

        if username and password:
            user = storage.check_user(username)
            
            if not user:
                return render_template("authenticate/login.html")

            if check_password_hash(user.password, password):
                user.authenticated = True
                user.save()
                login_user(user)

                next = request.args.get('next')

                return redirect(next or url_for('profile_views.profile_page'))
            
    return render_template("authenticate/login.html")

@authenticate_views.route("/signup", methods=["GET", "POST"], strict_slashes=False)
def signup():
    if request.method == "POST":
        data = {
            'username': request.form.get("username", None),
            'first_name': request.form.get("first_name", None),
            'middle_name': request.form.get("middle_name", None),
            'last_name': request.form.get("last_name", None),
            'email': request.form.get("email", None),
            'password': request.form.get("password", None),
            're_password': request.form.get("re_password", None),
        }
        
        required_fields = ['username', 'first_name', 'last_name',
                           'email', 'password', 're_password'
                        ]

        for val in required_fields:
            if not data[val]:
                render_template("authenticate/signup.html")

        
        if data['password'] != data['re_password']:
            return render_template("authenticate/signup.html")

        data['password'] = generate_password_hash(data['password'])

        if storage.check_user(data['username']) and storage.check_email(data['email']):
            return render_template("authenticate/signup.html")

        del data["re_password"]
        user = User(**data)
        user.is_authenticated = True
        user.save()

        return redirect(url_for("authenticate_views.login"))

    return render_template("authenticate/signup.html")


@authenticate_views.route("/logout", methods=["GET", "POST"], strict_slashes=False)
@login_required
def logout():
    user = current_user
    user.authenticated = False
    user.save()
    logout_user()
    return redirect(url_for("landing_views.landing_page"))

