import json
from types import SimpleNamespace
import requests

from base.face_result import FaceResult
from base.result import Result


class GithubFace:

     def __init__(self, username) -> None:
        self.username = username
        self.base_url = f"https://api.github.com/users/{self.username}/events"

     def get_image(self):
        json_result = requests.get(self.base_url)
        github = json.loads(json_result.content, object_hook=lambda d: SimpleNamespace(**d))
        try:
            if(github.message):
                return FaceResult(status=Result.NOT_FOUND,url="", error=github.message)
        except AttributeError:
            pass

        try: 
            avatar_url = github[0].actor.avatar_url
            return FaceResult(status=Result.FOUND,url=avatar_url, error="None")
        except Exception:
             return FaceResult(status=Result.NOT_FOUND,url="", error="failure")