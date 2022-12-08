import re
from base.cloudflare_scrape import CloudFlareScrape
from base.scrape import Scrape

class AcademiaEduFace(Scrape):

    def __init__(self, username) -> None:
        self.username = username
        self.base_url = f"https://independent.academia.edu/{self.username}"

    def extracter(self, element):
        element_src = (element[0]["src"])
        return f"https://{element_src}";

    def get_image(self):
        return super().get_image(".profile-avatar", extract_function=self.extracter) 


       
