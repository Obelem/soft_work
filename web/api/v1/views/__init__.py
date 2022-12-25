#!/usr/bin/python3
'''initialize blueprint'''
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from web.api.v1.views import status
from web.api.v1.views import refresh_user
