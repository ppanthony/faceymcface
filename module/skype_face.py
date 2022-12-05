from base.face_result import FaceResult
from base.image_check import ImageCheck
from base.result import Result

class SkypeFace(ImageCheck):
    def __init__(self, username) -> None:
        self.username = username

    def get_url_of_image(self):
        url  = f"https://avatar.skype.com/v1/avatars/{self.username}/public"
        return url

    def determine_if_image_valid(self):
        url_to_check = self.get_url_of_image()
        return super().determine_if_image_valid(url_to_check, (180, 228, 251), 'Looks like Skype default')

    
    def get_image(self) -> FaceResult:
        try:
            return self.determine_if_image_valid()
        except Exception as e:
            print(e)
            return FaceResult(status=Result.ERROR, url="", error=str(e))