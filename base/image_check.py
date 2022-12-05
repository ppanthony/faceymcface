from base.face_result import FaceResult
from base.result import Result
import hashlib
from PIL import Image
import requests
from colorthief import ColorThief

class ImageCheck:
    
    def determine_if_image_valid(self, url_to_check, dominant_color_check, error):
        # check status code
        image_file = requests.get(url_to_check, stream=True).raw
        color_thief = ColorThief(image_file);
        dominant_color = color_thief.get_color(quality=1)
        # if gravatar default
        if dominant_color == (dominant_color_check):
         return FaceResult(status=Result.NOT_FOUND,url="", error=error)

        return FaceResult(status=Result.FOUND,url=url_to_check, error="")