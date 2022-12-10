from flask import Blueprint

authenticate_views = Blueprint("authenticate_views", __name__)

from web.views.access import *