# utils/imagekit.py

import base64
import requests
from django.conf import settings
import uuid

def upload_to_imagekit(file, file_name=None):
    url = "https://upload.imagekit.io/api/v1/files/upload"

    headers = {
        "Authorization": "Basic " + base64.b64encode(
            f"{settings.IMAGEKIT_PRIVATE_KEY}:".encode()
        ).decode()
    }
    unique_name = file_name or f"{uuid.uuid4().hex}_{file.name}"

    data = {
        "fileName": unique_name,
    }
    files = {
        "file": file,
    }

    response = requests.post(url, headers=headers, files=files , data=data)

    if response.status_code == 200:
        return response.json()["url"]
    else:
        raise Exception(f"ImageKit upload failed: {response.text}")
