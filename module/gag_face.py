import re
from base.cloudflare_scrape import CloudFlareScrape
from base.scrape import Scrape

class GagFace(CloudFlareScrape):

    def __init__(self, username) -> None:
        self.username = username
        self.base_url = f"https://9gag.com/u/{self.username}"

    def extracter(self, element):
        element_src = (element[0]["src"])
        return f"{element_src}";

    def get_image(self):
        return super().get_image(".avatar img", extract_function=self.extracter) 


       
