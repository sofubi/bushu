import requests

from typing import Optional
from concurrent.futures import ThreadPoolExecutor
from requests.models import Response
from requests.sessions import Session

class Client:
    session: Session = requests.Session()

    def __init__(self,
                 username: Optional[str] = None,
                 password: Optional[str] = None
                 ) -> None:
        self.__password = password
        self.__pool = ThreadPoolExecutor(max_workers=5)
        self.__username = username

    def login(self) -> None:
        url = 'https://mangadex.org/ajax/actions.ajax.php?function=login'
        header = {'x-requested-with': 'XMLHttpRequest'}
        payload = {
            'login_username': self.__username,
            'login_password': self.__password
        }
        self.session.post(
            url,
            data=payload,
            headers=header
        )

    def fetch(self, url: str) -> Response:
        resp = self.session.get(url)
        return resp

    def fetch_with_pool(self, urls: list) -> list:
        pages = []
        for page in self.__pool.map(self.fetch, urls):
            pages.append(page.content)
        return pages
