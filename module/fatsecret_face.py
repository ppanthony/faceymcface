import json
import re
import requests
from types import SimpleNamespace
from base.face_result import FaceResult
from base.result import Result
from base.scrape import Scrape


class FatSecretFace(Scrape):
    def __init__(self, username) -> None:
        self.username = username
        self.base_url = f"https://www.fatsecret.com/member/{self.username}"

    def extracter(self, element):
        element_src = element[0]["src"]
        return f"{element_src}"

    def get_image(self):
        return super().get_image(".memberProfileLrg .memberImage", extract_function=self.extracter)
