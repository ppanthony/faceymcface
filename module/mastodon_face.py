import re
from base.scrape import Scrape

class MastodonFace(Scrape):

    def __init__(self, username) -> None:
        self.username = username
        self.base_url = f"https://mastodon.cloud/@{self.username}"

    def extracter(self, element):
        src = (element[0]["src"])
        return src

    def get_image(self):
        return super().get_image("img#profile_page_avatar", extract_function=self.extracter) 


       
        
