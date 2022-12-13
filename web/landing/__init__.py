from flask import Blueprint

landing_views = Blueprint("landing_views", __name__,
                        template_folder='templates'
                        )

from web.landing.routes import *