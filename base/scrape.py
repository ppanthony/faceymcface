import requests
from bs4 import BeautifulSoup
from base.face_result import FaceResult
from base.result import Result
import re


class Scrape:
    def get_page(self, timeout):
        page = requests.get(self.base_url)
        return page.content

    def get_image(self, selector, extract_function, timeout=5):
        try:
            page = self.get_page(timeout)
            soup = BeautifulSoup(page, "html.parser")
            element = soup.select(selector)
            match = extract_function(element)
            return FaceResult(status=Result.FOUND, url=match, error="")

        except Exception as e:
            print(e)
            return FaceResult(status=Result.ERROR, url="", error=str(e))
