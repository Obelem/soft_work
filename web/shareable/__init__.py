from flask import Blueprint

shareable_views = Blueprint("shareble_views", __name__,
                            template_folder='templates'
                            )

from web.shareable.shareable import *