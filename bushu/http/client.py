import requests
from concurrent.futures import ThreadPoolExecutor
from requests.models import Response


class Client:
    session = None

    def __init__(self, username: str, password: str) -> None:
        self.session = requests.Session()
        self.login(username, password)
        self.pool = ThreadPoolExecutor(max_workers=5)

    def login(self, username: str, password: str) -> None:
        url = 'https://mangadex.org/ajax/actions.ajax.php?function=login'
        header = {'x-requested-with': 'XMLHttpRequest'}
        payload = {
            'login_username': username,
            'login_password': password
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
        for page in self.pool.map(self.fetch, urls):
            pages.append(page.content)
        return pages
