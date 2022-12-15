from flask import Blueprint

assessment_views = Blueprint("assessment_views", __name__,
                                template_folder='templates'
                            )

from web.assessment.routes import *
