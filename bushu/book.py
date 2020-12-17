import os

from typing import Any, ClassVar, Dict, List, Optional, Union
from bushu.http.client import Client


class Book:
    base_chapter_url: ClassVar[str] = "https://mangadex.org/api/v2/chapter"
    base_manga_url: ClassVar[str] = "https://mangadex.org/api/v2/manga"

    def __init__(self,
                 client: Client,
                 identifier: Optional[str] = None,
                 chapter_number: Optional[int] = 1,
                 directory: Union[str, os.PathLike[str]] = os.getcwd()
                 ) -> None:
        self.__chapter_number = chapter_number
        self.__client = client
        self.__directory = directory
        self.__identifier = identifier
        self.__pages: List[str] = []
        self.__all_chapters: Dict[int, Any] = {}
        self.__server: str = ''

    @property
    def chapter_number(self) -> int:
        return self.__chapter_number

    @chapter_number.setter
    def chapter_number(self, chapter_number: int) -> None:
        self.__chapter_number = chapter_number

    @chapter_number.getter
    def chapter_number(self) -> int:
        return self.chapter_number

    @property
    def directory(self) -> Union[str, os.PathLike[str]]:
        return self.__directory

    @directory.setter
    def directory(self, directory_name: str) -> None:
        self.__directory = directory_name

    @directory.getter
    def directory(self) -> Union[str, os.PathLike[str]]:
        return self.__directory

    @property
    def manga_url(self) -> str:
        return f'{self.base_manga_url}/{self.__identifier}'

    @manga_url.setter
    def manga_url(self, identifier: str) -> None:
        self.__identifier = identifier

    def enumerate_chapters(self) -> None:
        request = self.__client.fetch(f"{self.manga_url}/chapters")
        response = request.json()['data']['chapters']
        chapters = {}
        for r in response:
            if r['language'] == 'gb':
                chapters[int(r['chapter'])] = r['hash']
        chapters = {
            k: v for k, v in sorted(chapters.items(), key=lambda item: item[0])
        }
        self.__all_chapters = chapters

    def get_chapter_data(self) -> None:
        request = self.__client.fetch(
            f'{self.base_chapter_url}/'
            f'{self.__all_chapters[self.__chapter_number]}'
        )
        response = request.json()['data']
        self.__server = f"{response['server']}{response['hash']}"
        for p in response['pages']:
            self.__pages.append(f"{self.__server}/{p}")

    def download_pages(self) -> None:
        pages = self.__client.fetch_with_pool(self.__pages)
        os.makedirs(self.directory,
                    exist_ok=True)
        for i, p in enumerate(pages):
            with open(os.path.join(
                self.directory,
                f'{i}.png'
            ), 'wb'
            ) as fd:
                fd.write(p)
