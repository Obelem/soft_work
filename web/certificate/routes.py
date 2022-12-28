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
    certificate = current_user.certificate

    if not assessment:
        abort(404)

    completed = getattr(current_user.status, assessment.name)
    if completed != 'done':
        setattr(certificate, assessment.name, False)
        certificate.save()
        return {'state': completed}

    score = getattr(current_user.score, assessment.name)
    if score < 50:
        setattr(certificate, assessment.name, False)
        certificate.save()
        return {"state": score}

    setattr(certificate, assessment.name, True)
    certificate.save()

    data = {
        "awardee_name": f"{current_user.first_name} {current_user.last_name}" ,
        "assessment": assessment.name.replace("_", " "),
        "signature1": "frankinobasy",
        "certifier1": "Franklin Obasi",
        "certifier_title1": "co-founder, softwork",
        "signature2": "jesseobelem",
        "certifier2": "Jesse Obelem",
        "certifier_title2": "co-founder, softwork",
        "signature3": "amarachi",
        "certifier3": "Amarachi",
        "certifier_title3": "co-founder, softwork",
        "date": datetime.now().strftime("%d %B, %Y")
    }

    url = get_url(data)
    if url:
        name = f"{current_user.username}_{assessment.name}"
        filename = save_from_url(url, name)
        if save_to_aws(filename, "certificates"):
            link = get_aws_s3_link(name, "certificates")
            os.remove(filename)
            if not link:
                abort(404, description="Unable to get s3 link")
        else:
            abort(404, "Unable to upload to s3 bucket")
    else:
        abort(404, description="Could not generate certiicate url from data")


    return render_template('index.html', image_url=link)

    
