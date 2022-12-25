from datetime import datetime
import os
from flask import abort, render_template, send_file
from flask_login import current_user, login_required
from models import storage

from web.certificate import certificate_views

from web.tools.certificates import get_image, save_image, send_user_data, template
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
        'awardee_name': current_user.first_name,
        'details': f'The Above name is passed {assessment.name} skill test',
        'signature': 'franklinobasy',
        'signee': 'Franklin Obasi',
        'date': date,
    }

    image_uid = send_user_data(data, template)
    res = get_image(image_uid)
    image_url = res.get("image_url_png")
    save = save_image(res, filename=current_user.username)
    if not save:
        print("upload failed!")
        abort(404)

    return render_template('index.html', image_url=image_url)

    
