#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage



@app_views.route('/results', methods=['GET', 'POST'],
                strict_slashes=False)
def evaluate_results():
    if request.method == 'POST':
        return jsonify({'status': 'ok'}), 201
