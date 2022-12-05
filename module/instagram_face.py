from base.cloudflare_scrape import CloudFlareScrape


class InstagramFace(CloudFlareScrape):
    def __init__(self, username) -> None:
        self.username = username
        self.base_url = f"https://www.picuki.com/profile/{self.username}"

    def extracter(self, element):
        element_src = (element[0]["src"])
        return f"{element_src}";

    def get_image(self):
        return super().get_image(".profile-avatar-image", extract_function=self.extracter) 