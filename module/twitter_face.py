import re
from base.scrape import Scrape

class TwitterFace(Scrape):

    def __init__(self, username) -> None:
        self.username = username
        self.base_url = f"https://nitter.net/{self.username}"

    def extracter(self, element):
        element_src = (element[0]["src"])
        return f"https://nitter.net{element_src}";

    def get_image(self):
        return super().get_image(".profile-card-avatar img", extract_function=self.extracter) 


       
        
