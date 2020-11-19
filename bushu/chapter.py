from PIL import Image
import requests
from .manga import Manga


class Chapter:
    base_url = "https://mangadex.org/api/v2/chapter"

    def __init__(self, identifier, chapter_number):
        self.__manga = Manga(identifier)
        self.__chapter_number = chapter_number
        self.__server = None
        self.__pages = []

    def get_chapter_data(self):
        request = requests.get(
            f"{self.base_url}/{self.__manga.all_chapters[self.__chapter_number]}"
        )
        response = request.json()['data']
        self.__server = f"{response['server']}{response['hash']}"
        for p in response['pages']:
            self.__pages.append(f"{self.__server}/{p}")

    def open_page(self):
        response = requests.get(
            f"{self.__pages[0]}",
            stream=True
        )
        img = Image.open(response.raw)
        img.show()