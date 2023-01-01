import re
from base.scrape import Scrape
from base.cloudflare_scrape import CloudFlareScrape

class AirbitFace(CloudFlareScrape):

    def __init__(self, username) -> None:
        self.username = username
        self.base_url = f"https://airbit.com/{self.username}"

    def extracter(self, element):
        element_src = (element[0]["src"])
        return f"{element_src}";

    def get_image(self):
        return super().get_image(".single-producer__header__info_avatar", extract_function=self.extracter) 


       
        
