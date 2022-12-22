import json
import time
from uuid import uuid4
from datetime import datetime
from typing import Any
import requests
import urllib
import os

template = "n1MJGd520gN9b7LaPV"

def send_user_data(data: dict, template: str) -> Any:
    '''
    Sends user data for certificate creation
    '''
    
    if data:
        required = ['awardee_name', "details", "signature", "signee",
                    "date"
                    ]
        missing = []
        for val in data.keys():
            if val not in required:
                missing.append(val)
        if missing:
            print({"Error": f"Some required information are missing: {missing}"})
            return None

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer bb_pr_39c8e4026d4a758e6c85c587fda5e0'
    }

    payload = {
        "template": template,
        "modifications": [
            {
                "name": "pretitle",
                "text": "certificate of",
                "color": None,
                "background": None
            },
            {
                "name": "title",
                "text": "Completion",
                "color": None,
                "background": None
            },
            {
                "name": "awardee_name",
                "text": data['awardee_name'],
                "color": None,
                "background": None
            },
            {
                "name": "details",
                "text": data["details"],
                "color": None,
                "background": None
            },
            {
                "name": "signature",
                "text": data['signature'],
                "color": None,
                "background": None
            },
            {
                "name": "signee",
                "text": data['signee'],
                "color": None,
                "background": None
            },
            {
                "name": "date",
                "text": data['date'],
                "color": None,
                "background": None
            },
            {
            "name": "date_title",
            "text": "Date Issued",
            "color": None,
            "background": None
            }
        ],
        "webhook_url": None,
        "transparent": False,
        "metadata": None
    }

    payload = json.dumps(payload)

    response = requests.post(
        url="https://api.bannerbear.com/v2/images",
        data=payload,
        headers=headers,
        
        )

    response = response.json()
    time.sleep(1.0)
    return response.get("uid")

def get_image(image_uid: str) -> str:

    headers = {
        'Authorization': 'Bearer bb_pr_39c8e4026d4a758e6c85c587fda5e0'
    }

    response = requests.get(
        url=f"https://api.bannerbear.com/v2/images/{image_uid}",
        headers=headers,
    )
    return response.json()

def save_image(res, filename="test") -> bool:
    '''
    save image from url to uploads folder
    '''

    filepath = os.getcwd() + "/uploads/certs_img"
    if not os.path.isdir(filepath):
        os.makedirs(filepath)

    filename = f"{filepath}/{filename}.png"
    if res.get("status") == "completed":
        image_url = res.get("image_url_png")
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','SoftWork')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(image_url, filename)
        # print('Image sucessfully Downloaded: ',filename)
        return True
    else:
        print('Image Couldn\'t be retrieved')
        return False

if __name__ == "__main__":
    from datetime import datetime
    date = datetime.now()
    date = date.strftime("%A %m %Y")

    data = {
        'awardee_name': 'John Doe',
        'details': 'The Above name is now a software engineer',
        'signature': 'franklinobasy',
        'signee': 'Franklin Obasi',
        'date': date,
    }

    image_uid = send_user_data(data, template)
    res = get_image(image_uid)
    save = save_image(res, filename="user001")
    if save:
        print("upload successfull!")
    else:
        print("upload failed!")    
