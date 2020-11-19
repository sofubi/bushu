import requests

class Manga:
    base_url = "https://mangadex.org/api/v2/manga/"

    def __init__(self, identifier):
        self.__identifier = identifier
        self.__url = ''
        self.__title = ''
        self.all_chapters = None
        self.update_url()
        self.enumerate_chapters()

    @property
    def identifier(self):
        return self.__identifier

    @identifier.getter
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier):
        self.__identifier = identifier

    @property
    def url(self):
        return self.__url

    @url.getter
    def url(self):
        return self.__url

    def update_url(self):
        self.__url = f"{self.base_url}{self.__identifier}"

    @property
    def title(self):
        return self.__title

    @title.getter
    def title(self):
        return self.__title

    def fetch_title(self, identifier):
        self.update_url()
        request = requests.get(self.__url)
        self.__title = f"{request.json()['data']['title']}"

    def enumerate_chapters(self):
        request = requests.get(f"{self.__url}/chapters")
        response = request.json()['data']['chapters']
        chapters = {}
        for r in response:
            if r['language'] == 'gb':
                chapters[int(r['chapter'])] = r['hash']
        chapters = {
            k: v for k, v in sorted(chapters.items(), key=lambda item: item[0])
        }
        self.all_chapters = chapters