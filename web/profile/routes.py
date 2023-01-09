from flask import abort, jsonify, render_template, request, url_for, flash, redirect
from web.profile import profile_views
from flask_login import login_required, current_user, login_user
from models.user import User
from models import storage

from web.tools.certificates1 import get_aws_s3_link
from werkzeug.security import generate_password_hash, check_password_hash



@profile_views.route("/", methods=['GET'])
@login_required
def profile_page():
    if not current_user.profile_pic:
        link = get_aws_s3_link("default", "dps")
    else:
        name = current_user.profile_pic_name
        link = get_aws_s3_link(name, "dps", category="profile picture")
        current_user.profile_pic = True
        storage.save()

    return render_template(
        "profile/profile.html",
        first_name=current_user.first_name,
        last_name=current_user.last_name,
        middle_name=current_user.middle_name,
        username = current_user.username,
        status = current_user.status,
        assessments = storage.all('Assessment').values(),
        score = current_user.score,
        user_id = current_user.id,
        profile_pic = link
    )


@profile_views.route("/edit", methods=['GET', 'POST'], strict_slashes=False)
@login_required
def edit_profile():
    if request.method == 'GET':
        return render_template('profile/edit-profile.html')

    if request.method == 'POST':
        '''edit user info'''
        data = request.form.to_dict()

        if data.get('password'):
            if check_password_hash(current_user.password, data['password']):
                data['password'] = generate_password_hash(data['new_password'])
                del data['new_password']
            else:
                flash("Password incorrect")
                return redirect(url_for('profile_views.edit_profile'))

        if data['email'] and storage.check_email(data['email']):
            flash(f"Email already exists, try another one")
            return redirect(url_for("profile_views.edit_profile"))

        for key, value in data.items():
            if data[key]:
                setattr(current_user, key, value)

        current_user.save()

        if data['password']:
            login_user(current_user)

        return redirect(url_for('profile_views.profile_page'))
