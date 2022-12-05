import json
import random
import requests
from base.cloudflare_scrape import CloudFlareScrape
from base.face_result import FaceResult
from base.image_check import ImageCheck
from base.result import Result
from base.scrape import Scrape

class YoutubeFace(CloudFlareScrape):
    def __init__(self, username) -> None:
            self.username = username
            self.base_url = f"https://www.youtube.com/user/{self.username}"

    def get_page(self, timeout):
        page = requests.get(self.base_url)
        page = requests.get(self.base_url, cookies={'CONSENT': 'PENDING+999'})
        page = requests.get(self.base_url, cookies={'CONSENT': 'YES+cb.20210328-17-p0.en-GB+FX+{}'.format(random.randint(100, 999))})
        return page.content

    def extracter(self, element):
            element_src = (element[0]["href"])
            return f"{element_src}";

    def get_image(self):
            return super().get_image("link[itemprop='thumbnailUrl']", extract_function=self.extracter) 
