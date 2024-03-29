import requests
from datetime import datetime
import json
import os
import urllib

from web.tools.aws import upload_file, create_presigned_url


def get_url(data: dict) -> str:
    '''
    This function is used to generate a certificate from the data
    supplied. It returns the url of the certificate generated (png)

    :param data: data to generate
    :return url if successful else None
    '''
    url = "https://api.canvas.switchboard.ai/"
    headers = {
        "X-API-Key": "aeae59cd-5e25-4224-b09f-7c6d75888f8c",
        "Content-Type": "application/json",
    }

    payload = {
        "template": "softworkcertificate",
        "sizes": [
            {
                "width": 1920,
                "height": 1080
            }
        ],
        "elements" : {
            "awardee_name": {
                "text": data.get("awardee_name", "")
            },
            "assessment": {
                "text": data.get("assessment", "")
            },
            "signature1": {
                "text": data.get("signature1", "")
            },
            "certifier1": {
                "text": data.get("certifier1", "")
            },
            "certifier_title1": {
                "text": data.get("certifier_title1", "")
            },
            "signature2": {
                "text": data.get("signature2", "")
            },
            "certifier2": {
                "text": data.get("certifier2", "")
            },
            "certifier_title2": {
                "text": data.get("certifier_title2", "")
            },
            "signature3": {
                "text": data.get("signature3", "")
            },
            "certifier3": {
                "text": data.get("certifier3", "")
            },
            "certifier_title3": {
                "text": data.get("certifier_title3", "")
            },
            "date": {
                "text": data.get("date", "")
            },
        }
    }
    response = requests.post(
        url=url,
        data=json.dumps(payload),
        headers=headers,
    )

    response = response.json().get("sizes", None)

    if not response:
        return None

    return response[0].get('url', None)

def save_from_url(url, filename):
    '''
    saves image from url to upload-folder

    :param url: url of image to save
    :param filename: name of file to save as (excluding file extention)
    :return filepath if saved successfully else False
    '''

    filepath = os.getcwd() + "/uploads/certs_img"
    if not os.path.isdir(filepath):
        os.makedirs(filepath)

    filename = f"{filepath}/{filename}.png"
    if url:
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','SoftWork')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url, filename)
        # print('Image sucessfully Downloaded: ',filename)
        return filename
    else:
        print('Image Couldn\'t be retrieved')
        return False

def save_to_aws(filename: str, folder=None):
    '''
    Uploads file to aws s3 folder

    :param filename: filepath of file to upload
    :folder: name of s3 folder
    :return True if object is saved else False
    '''
    if filename:
        bucket_name = "fo-softwork-02"
        if folder:
            object_name = f"{folder}/{filename.split('/')[-1]}"
        else:
            object_name = None

        res = upload_file(filename, bucket_name, object_name)
        if res:
            return True

    return False

def get_aws_s3_link(name, folder=None, category=None):
    '''
    generate url of file with name from a folder in s3 bucket

    :param name: object key name
    :param folder: object's folder
    '''
    if category == "profile picture":
        object_name = name
    else:
        object_name = name + ".png"
        
    bucket_name = "fo-softwork-02"
    if folder:
        object_name = f"{folder}/{object_name}"

    res = create_presigned_url(bucket_name, object_name)
    if not res:
        return False

    return res




if __name__ == "__main__":
    data = {
        "awardee_name": "Femi Lawson",
        "assessment": "Listening Skills",
        "signature": "johnnybravo",
        "certifier": "John Bravo",
        "certifier_title": "Teacher",
        "date": datetime.now().strftime("%A %m %Y")
    }

    url = get_url(data)
    if url:
        filename = save_from_url(url, "demo")
        if save_to_aws(filename, "certificates"):
            print("successfully uploaded to aws s3 bucket")
            link = get_aws_s3_link("demo", "certificates")
            if link:
                print(link)
            else:
                print("Unable to get link for object")
        else:
            print("failed to upload to aws bucket")
    else:
        print("error")