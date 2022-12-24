#!/usr/bin/python3
'''views for assessment status of current user'''
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage


@app_views.route('/status/<user_id>',
                 strict_slashes=False)
def get_status(user_id):
    '''retrieves assessment status of current user'''
    user = storage.get('User', user_id)
    status = user.status
    return jsonify(status.to_dict())
