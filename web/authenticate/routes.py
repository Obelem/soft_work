
from flask import abort, jsonify, redirect, request, render_template, url_for, flash
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
                flash('Username does not exist.')
                return redirect(url_for('authenticate_views.login'))

            if check_password_hash(user.password, password):
                user.authenticated = True
                user.save()
                login_user(user)

                next = request.args.get('next')

                return redirect(next or url_for('profile_views.profile_page'))
            else:
                flash("Username/Password incorrect")
                return redirect(url_for('authenticate_views.login'))
        else:
            flash("Username/Password field is empty")
            return redirect(url_for('authenticate_views.login'))

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
                flash(f"{val} field is empty")
                redirect(url_for("autenticate_views.signup"))


        if data['password'] != data['re_password']:
            flash(f"Password mismatch")
            redirect(url_for("autenticate_views.signup"))

        data['password'] = generate_password_hash(data['password'])

        if storage.check_user(data['username']):
            flash(f"Username is already chosen, try another one!")
            redirect(url_for("autenticate_views.signup"))

        if storage.check_email(data['email']):
            flash(f"Email already exists, try another one")
            redirect(url_for("autenticate_views.signup"))

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

