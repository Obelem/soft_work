from flask import Blueprint

profile_views = Blueprint("profile_views", __name__,
                        template_folder="templates", static_folder="static",
                        )

from web.profile.routes import *
