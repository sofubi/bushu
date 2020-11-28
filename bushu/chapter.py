from bushu.http.client import Client
from bushu import Manga
import os


class Chapter:
    base_url = "https://mangadex.org/api/v2/chapter"

    def __init__(self, client: Client, identifier: str, chapter_number: int):
        self.__manga = Manga(client, identifier)
        self.__chapter_number = chapter_number
        self.__server = None
        self.__pages = []
        self.__client = client

    def get_chapter_data(self) -> None:
        request = self.__client.fetch(
            f"{self.base_url}/{self.__manga.all_chapters[self.__chapter_number]}"
        )
        response = request.json()['data']
        self.__server = f"{response['server']}{response['hash']}"
        for p in response['pages']:
            self.__pages.append(f"{self.__server}/{p}")

    def download_pages(self) -> None:
        pages = self.__client.fetch_with_pool(self.__pages)
        os.makedirs('',
                    exist_ok=True)
        for i, p in enumerate(pages):
            with open(os.path.join(
                '',
                f'{i}.png'
            ), 'wb'
            ) as fd:
                fd.write(p)
