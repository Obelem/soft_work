from flask import Blueprint

profile_views = Blueprint("profile_views", __name__, 
                        template_folder="templates"
                        )

from web.profile.routes import *