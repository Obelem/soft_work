#!/usr/bin/python3
'''views for assessment status of current user'''
from web.api.v1.views import app_views
from flask import jsonify, abort, request, redirect, url_for, render_template
from flask_login import login_required, current_user, logout_user
from models import storage


@app_views.route('/delete_user', methods=['DELETE'],
                strict_slashes=False)
@login_required
def delete_user():
    storage.delete(current_user)
    storage.save()

    return jsonify({'deleted': True})
