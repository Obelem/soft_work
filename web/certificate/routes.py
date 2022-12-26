from datetime import datetime
import os
from flask import abort, render_template, send_file
from flask_login import current_user, login_required
from models import storage
from models.certificate import Certificate

from web.certificate import certificate_views

from web.tools.certificates1 import get_url, get_aws_s3_link, save_from_url, save_to_aws
from web.tools.aws import upload_file, create_presigned_url


@certificate_views.route("/<accessment_id>")
@login_required
def load_cert(accessment_id):
    date = datetime.now()
    date = date.strftime("%A %m %Y")

    assessment = storage.get('Assessment', accessment_id)

    if not assessment:
        abort(404)

    completed = getattr(current_user.status, assessment.name)
    if completed != 'done':
        return {'state': completed}

    score = getattr(current_user.score, assessment.name)
    if score < 50:
        return {"state": score}


    data = {
        "awardee_name": f"{current_user.first_name} {current_user.last_name}" ,
        "assessment": assessment.name.replace("_", " "),
        "signature": "frankinobasy",
        "certifier": "Franklin Obasi",
        "certifier_title": "co-founder, softwork",
        "date": datetime.now().strftime("%A %m %Y")
    }

    url = get_url(data)
    if url:
        name = f"{current_user.username}_{assessment.name}"
        filename = save_from_url(url, name)
        if save_to_aws(filename, "certificates"):
            link = get_aws_s3_link(name, "certificates")
            if not link:
                abort(404, description="Unable to get s3 link")
        else:
            abort(404, "Unable to upload to s3 bucket")
    else:
        abort(404, description="Could not generate certiicate url from data")


    return render_template('index.html', image_url=link)

    
