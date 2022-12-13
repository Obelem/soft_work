from flask import Blueprint

authenticate_views = Blueprint("authenticate_views", __name__, 
                                template_folder='templates',
                                static_folder='static'
                                )

from web.authenticate.routes import *