from module.academia_edu_face import AcademiaEduFace
from module.cups_face import CupsFace
from module.gag_face import GagFace
from base.result import Result
from module.aboutme_face import AboutMeFace
from module.bitwarden_face import BitwardenFace
from module.facebook_face import FacebookFace
from module.github_face import GithubFace
from module.gravatar_face import GravatarFace
from module.imgur_face import ImgurFace
from module.instagram_face import InstagramFace
from module.mastodon_face import MastodonFace
from module.skype_face import SkypeFace
from module.brave_face import BraveFace
from module.tiktok_face import TikTokFace
from module.tinder_face import TinderFace
from module.twitter_face import TwitterFace
import asyncio
from colorama import Fore

from module.youtube_face import YoutubeFace

class FaceyMcFace:
    def __init__(self, email_address, username) -> None:
        self.email_address = email_address
        self.username = username
        self.results = []

    async def get_gravatar(self):
        gravatar = GravatarFace(self.email_address)
        result = gravatar.get_image()
        if result.status == Result.FOUND:
           self.results.append(result.url)
        return None
    
    async def get_skype(self):
        gravatar = SkypeFace(self.username)
        result = gravatar.get_image()
        if result.status == Result.FOUND:
           self.results.append(result.url)
        return None

    async def get_aboutme(self):
        gravatar = AboutMeFace(self.username)
        result = gravatar.get_image()
        if result.status == Result.FOUND:
           self.results.append(result.url)
        return None

    async def get_bitwarden(self):
        gravatar = BitwardenFace(self.username)
        result = gravatar.get_image()
        if result.status == Result.FOUND:
           self.results.append(result.url)
        return None

    async def get_github(self):
        gravatar = GithubFace(self.username)
        result = gravatar.get_image()
        if result.status == Result.FOUND:
          self.results.append(result.url)
        return None

    async def get_brave(self):
        avatar = BraveFace(self.username)
        result = avatar.get_image()
        if result.status == Result.FOUND:
          self.results.append(result.url)
        return None

    async def get_twitter(self):
        avatar = TwitterFace(self.username)
        result = avatar.get_image()
        if result.status == Result.FOUND:
           self.results.append(result.url)
        return None

    async def get_facebook(self):
        avatar = FacebookFace(self.username)
        result = avatar.get_image()
        if result.status == Result.FOUND:
          self.results.append(result.url)
        return None

    async def get_instagram(self):
        avatar = InstagramFace(self.username)
        result = avatar.get_image()
        if result.status == Result.FOUND:
          self.results.append(result.url)
        return None

    async def get_imgur(self):
        avatar = ImgurFace(self.username)
        result = avatar.get_image()
        if result.status == Result.FOUND:
           self.results.append(result.url)
        return None

    async def get_tinder(self):
        avatar = TinderFace(self.username)
        result = avatar.get_image()
        if result.status == Result.FOUND:
           self.results.append(result.url)
        return None

    async def get_tiktok(self):
        print(f"Attempting to find Tiktok")
        avatar = TikTokFace(self.username)
        result = avatar.get_image()
        if result.status == Result.FOUND:
           print(f"FOUND!")
           self.results.append(result.url)
        return None

    async def get_mastodon(self):
        print(f"Attempting to find Mastodon")
        avatar = MastodonFace(self.username)
        result = avatar.get_image()
        if result.status == Result.FOUND:
           print(f"FOUND!")
           self.results.append(result.url)
        return None
        
    async def get_youtube(self):
        print(f"Attempting to find Youtube data")
        avatar = YoutubeFace(self.username)
        result = avatar.get_image()
        if result.status == Result.FOUND:
           print(f"FOUND!")
           self.results.append(result.url)
        return None

    async def get_9gag(self):
        gravatar = GagFace(self.username)
        result = gravatar.get_image()
        if result.status == Result.FOUND:
           self.results.append(result.url)
        return None

    async def get_7cups(self):
        gravatar = CupsFace(self.username)
        result = gravatar.get_image()
        if result.status == Result.FOUND:
           self.results.append(result.url)
        return None

    async def get_academiaedu(self):
        gravatar = AcademiaEduFace(self.username)
        result = gravatar.get_image()
        if result.status == Result.FOUND:
           self.results.append(result.url)
        return None

async def main():

    obj = FaceyMcFace(None,'blue')
    print(f"Attempting to lookup {obj.username}!")
    await asyncio.gather(
        obj.get_9gag(),
        obj.get_youtube(),
        obj.get_mastodon(),
        obj.get_tiktok(),
        obj.get_tinder(),
        obj.get_imgur(),
        obj.get_instagram(), 
        obj.get_facebook(),
        obj.get_aboutme(),
        obj.get_bitwarden(),
        obj.get_twitter(),
        obj.get_brave(),
        obj.get_github(),
        obj.get_skype(),
        obj.get_aboutme(),
        obj.get_bitwarden(),
        obj.get_7cups(),
        obj.get_academiaedu()
    )
    print(obj.results)

asyncio.run(main())
