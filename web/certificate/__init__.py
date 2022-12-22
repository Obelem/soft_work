from flask import Blueprint

certificate_views = Blueprint("certificate_views", __name__,
                        template_folder="templates"
                        )

from web.certificate.routes import *