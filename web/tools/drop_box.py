import os
from dotenv import load_dotenv
import dropbox
from dropbox import Dropbox
from os import environ
from typing import List

load_dotenv("./.env")
# access_token = environ["DROPBOX_ACCESS_TKN"]
access_token = "sl.BVhXlEMnN5ZxpWBuohw_cGmoJmFdd8L-CojVitRKEJg3AQE4Sbkt1Nbbk1FPJTHInXKooSo-t3dXocpZoz61OYAgF9khj7wdVAKnRvIOUcdCKh5vov_ptaSlxdD-TPskx_vvMPefOAxT"

def connect_to_dropbox(access_token: str) -> Dropbox:
    try:
        dbx = Dropbox(access_token)
        print('Connected to Dropbox successfully')
    except Exception as e:
        print(str(e))
      
    return dbx

def list_files(dbx: Dropbox) -> List[str]:
    files = []
    for file in dbx.files_list_folder("").entries:
        files.append(file.name)
    
    return files

def upload_file(dbx: Dropbox, path: str, filename: str) -> bool:
    try:
        with open(path, "rb") as f:
            meta = dbx.files_upload(f.read(), f"/{filename}.jpg", mode=dropbox.files.WriteMode("overwrite"))
    except FileNotFoundError as e:
        return {'Error', 'Unable to find file'}
    except Exception as e:
        return {'Error': f'Error uploading file to Dropbox: {str(e)}'}

def get_file_link(dropbox_filepath: str) -> str:
    try:
        dbx = connect_to_dropbox(access_token)
        shared_link_metadata = dbx.sharing_create_shared_link_with_settings(dropbox_filepath)
        shared_link = shared_link_metadata.url
        return shared_link.replace('?dl=0', '?dl=1')

    except dropbox.exceptions.ApiError as exception:
        if exception.error.is_shared_link_already_exists():
            shared_link_metadata = dbx.sharing_get_shared_links(dropbox_filepath)
            shared_link = shared_link_metadata.links[0].url
            return shared_link.replace('?dl=0', '?dl=1')

    except Exception as e:
        return {'Error': f'Unable to get file_link: {str(e)}'}

if __name__ == "__main__":
    username = "user001"
    dbx = connect_to_dropbox(access_token)
    filepath = os.getcwd() + "/uploads/certs_img"
    print(upload_file(dbx, f"{filepath}/{username}.png", username) )
    print(f"\n{get_file_link(f'/{username}.jpg')}")