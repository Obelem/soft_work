#!/usr/bin/python3
'''refresh score and status of user'''
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.user import User


@app_views.route('/refresh_user', methods=['PUT'],
                strict_slashes=False)
def refresh_user():
    '''view function to refresh user scores and status when
       restarting test
    '''
    if request.headers.get('Content-Type') != 'application/json':
            abort(400, description='Not a JSON')

    request_data = request.get_json()

    user_id = request_data.get('user_id')
    assessment_name = request_data.get('assessment_name')

    user = storage.get('User', user_id)

    setattr(user.score, assessment_name, None)
    setattr(user.status, assessment_name, None)

    storage.save()

    return jsonify([user.score.to_dict(), user.status.to_dict()])
