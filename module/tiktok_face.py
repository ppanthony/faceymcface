import re
from base.cloudflare_scrape import CloudFlareScrape
from base.face_result import FaceResult
from base.result import Result
from base.scrape import Scrape

class TikTokFace(CloudFlareScrape):
  
    def __init__(self, username) -> None:
        self.username = username
        self.base_url = f"https://tiktok.com/@{self.username}"

    def extracter(self, element):
        src = (element[0]["src"])
        return src

    def get_image(self):
        return super().get_image("div[data-e2e='user-page'] img[class*='-ImgAvatar']", extract_function=self.extracter, timeout=2) 

