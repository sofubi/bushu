from bushu.http.client import Client


class Manga:
    base_url: str = "https://mangadex.org/api/v2/manga/"

    def __init__(self, client: Client, identifier: str) -> None:
        self.__identifier = identifier
        self.__url = ''
        self.__title = ''
        self.__client = client
        self.all_chapters = None
        self.update_url()
        self.enumerate_chapters()

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.getter
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def url(self) -> str:
        return self.__url

    @url.getter
    def url(self) -> str:
        return self.__url

    def update_url(self) -> None:
        self.__url = f"{self.base_url}{self.__identifier}"

    @property
    def title(self) -> str:
        return self.__title

    @title.getter
    def title(self) -> str:
        return self.__title

    def fetch_title(self) -> None:
        self.update_url()
        request = self.__client.fetch(self.__url)
        self.__title = f"{request.json()['data']['title']}"

    def enumerate_chapters(self) -> None:
        request = self.__client.fetch(f"{self.__url}/chapters")
        response = request.json()['data']['chapters']
        chapters = {}
        for r in response:
            if r['language'] == 'gb':
                chapters[int(r['chapter'])] = r['hash']
        chapters = {
            k: v for k, v in sorted(chapters.items(), key=lambda item: item[0])
        }
        self.all_chapters = chapters
