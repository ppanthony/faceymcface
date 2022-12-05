from base.face_result import FaceResult
from base.image_check import ImageCheck
from base.result import Result

class BraveFace(ImageCheck):
    def __init__(self, username) -> None:
        self.username = username

    def get_url_of_image(self):
        url  = f"https://sea1.discourse-cdn.com/brave/user_avatar/community.brave.com/{self.username}/240/145408_2.png"
        return url

    def determine_if_image_valid(self):
        url_to_check = self.get_url_of_image()
        return super().determine_if_image_valid(url_to_check, (212, 212, 212), 'Looks like Brave default')

    
    def get_image(self) -> FaceResult:
        try:
            return self.determine_if_image_valid()
        except Exception as e:
            return FaceResult(status=Result.ERROR, url="", error=str(e))