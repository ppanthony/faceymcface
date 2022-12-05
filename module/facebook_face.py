import re
from base.scrape import Scrape

class FacebookFace(Scrape):

    def __init__(self, username) -> None:
        self.username = username
        self.base_url = f"https://m.facebook.com/{self.username}"

    def extracter(self, element):
        element_src = (element[2]["src"])
        return f"{element_src}";

    def get_image(self):
        return super().get_image("img", extract_function=self.extracter) 


       
        
