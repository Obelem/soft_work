from flask import jsonify, render_template, abort
from models.user import User
from models import storage
from web.tools.certificates1 import get_aws_s3_link
from web.shareable import shareable_views


@shareable_views.route("/<username>", 
                        methods=["GET"], 
                        strict_slashes=False)
def share_url(username):
    user = storage.check_user(username)
    if not user:
        abort(404, description="No such user")
    certificate = user.certificate
    assessments = storage.all("Assessment").values()
    assessment_names = [assessment.name for assessment in assessments]
    
    to_show = {}

    for name in assessment_names:
        if getattr(certificate, name):
            link = get_aws_s3_link(username, folder="certificates")
            to_show[name] = link

    return jsonify({f"{username}" : to_show})
