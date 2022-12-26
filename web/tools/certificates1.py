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
        "X-API-Key": "7197ce6c-469b-4b44-9377-b97ece965a68",
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
            "signature": {
                "text": data.get("signature", "")
            },
            "certifier": {
                "text": data.get("certifier", "")
            },
            "certifier_title": {
                "text": data.get("certifier_title", "")
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

def get_aws_s3_link(name, folder=None):
    '''
    generate url of file with name from a folder in s3 bucket

    :param name: object key name
    :param folder: object's folder
    '''
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