import json
import requests
from types import SimpleNamespace

from base.face_result import FaceResult
from base.result import Result

class BitwardenFace:

     def __init__(self, username) -> None:
        self.username = username
        self.base_url = f"https://community.bitwarden.com/u/{self.username}.json"

     def get_image(self):
        json_result = requests.get(self.base_url)
        bitwarden = json.loads(json_result.content, object_hook=lambda d: SimpleNamespace(**d))
        try:
            if(bitwarden.errors and len(bitwarden.errors) > 0):
                return FaceResult(status=Result.NOT_FOUND,url="", error=bitwarden.errors[0])
        except AttributeError:
            url = f"https://community.bitwarden.com/{bitwarden.user.avatar_template}".replace("{size}","480")
            return FaceResult(status=Result.FOUND,url=url, error="")
    