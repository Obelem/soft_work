#!/usr/bin/python3
'''views for assessment status of current user'''
from web.api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage


@app_views.route('/status/<user_id>',
                 strict_slashes=False)
def get_status(user_id):
    '''retrieves assessment status of current user'''
    user = storage.get('User', user_id)
    status = user.status
    return jsonify(status.to_dict())

@app_views.route("/dp_status/<user_id>", methods=["POST"])
def change_profile_pic(user_id):
    if request.method == "POST":
        if request.headers.get('Content-Type') == 'application/json':
            data = request.json

            if "status" in data  and type(data["status"]) == bool:
                user = storage.get('User', user_id)
                user.profile_pic = data["status"]
                user.save()
            return jsonify({'success': True})
    
    return jsonify({'success': False})


@app_views.route("/dp-name/<user_id>/<filename>", methods=["POST"])
def change_dp_filename(user_id, filename):
    if request.method == "POST":
        user = storage.get("User", user_id)
        if user:
            user.profile_pic_name = filename
            user.save()

            return jsonify({"success": True})
        
        return jsonify({"success": False})
    
    return jsonify({"error": "method not allowed"})