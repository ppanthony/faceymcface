import requests
from bs4 import BeautifulSoup
from base.face_result import FaceResult
from base.result import Result
from base.scrape import Scrape
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path # this will get you the path variable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium_stealth import stealth
import time

class CloudFlareScrape(Scrape):
    def get_page(self, timeout):
        service_object = Service(binary_path)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        # delay = 3
        
        browser = webdriver.Chrome(service=service_object, chrome_options=chrome_options)
        stealth(browser,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
        browser.get(self.base_url)
        time.sleep(timeout)
        html = browser.page_source
        browser.quit()
        return html