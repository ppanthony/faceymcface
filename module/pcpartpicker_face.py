from base.cloudflare_scrape import CloudFlareScrape
from base.scrape import Scrape


class PcPartPickerFace(CloudFlareScrape):
    def __init__(self, username) -> None:
        self.username = "Harper0921"
        self.base_url = f"https://pcpartpicker.com/user/{self.username}/"

    def extracter(self, element):
        element_src = element[0]["src"]
        return f"https://{element_src}"

    def get_image(self):
        return super().get_image(".user-avatar", extract_function=self.extracter)
