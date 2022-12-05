from base.cloudflare_scrape import CloudFlareScrape
from base.face_result import FaceResult
from base.image_check import ImageCheck
from base.result import Result


class ImgurFace(ImageCheck):
    def __init__(self, username) -> None:
        self.username = username

   
    def get_url_of_image(self):
        url  = 'https://imgur.com/user/' + self.username + '/avatar'
        return url


    def determine_if_image_valid(self):
        url_to_check = self.get_url_of_image()
        return super().determine_if_image_valid(url_to_check, (53, 204, 164), 'Looks like Imgur default')

    
    def get_image(self) -> FaceResult:
        try:
            return self.determine_if_image_valid()
        except Exception as e:
            return FaceResult(status=Result.ERROR, url="", error=str(e))
