import requests
from base.face_result import FaceResult
from base.image_check import ImageCheck
from base.result import Result

class ArduinoFace(ImageCheck):
    def __init__(self, username) -> None:
        self.username = username

    def get_url_of_image(self):
        url  = f"https://content.arduino.cc/avatars/2/{self.username}.jpeg"
        return url
    
    def get_image(self) -> FaceResult:
        try:
            url = self.get_url_of_image()
            content =  requests.get(url)
            if(content.status_code == 200):
                return FaceResult(status=Result.FOUND,url=url, error="")
            else:
                 return FaceResult(status=Result.ERROR, url="", error="Not found")
        except Exception as e:
            print(e)
            return FaceResult(status=Result.ERROR, url="", error=str(e))