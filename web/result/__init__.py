from flask import Blueprint

result_views = Blueprint("result_views", __name__,
                        template_folder="templates"
                        )

from web.result.routes import *
