
from base.face_result import FaceResult
from base.image_check import ImageCheck
from base.result import Result
import hashlib

class GravatarFace(ImageCheck):
     def __init__(self, email_address) -> None:
        self.email_address = email_address

     def md5_hash(self):
        hash_email = (hashlib.md5(self.email_address.encode())).hexdigest()
        return hash_email
    
     def get_url_of_image(self):
        hash_email = self.md5_hash()
        url  = 'https://gravatar.com/avatar/' + hash_email + '?s=1000'
        return url
        

     def determine_if_image_valid(self):
        url_to_check = self.get_url_of_image()
        return super().determine_if_image_valid(url_to_check, (12, 115, 179), 'Looks like Gravatar default')


     def get_image(self) -> FaceResult:
        try:
            return self.determine_if_image_valid()
        except Exception as e:
            print(e)
            return FaceResult(status=Result.ERROR, url="", error=str(e))