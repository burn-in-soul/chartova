from typing import Dict

import requests


class ChartovaRequest:
    _BASE_URL = 'https://www.nashe.ru/chartova/'

    def __init__(self, session: requests.Session) -> None:
        self._session = session

    def make(self, path: str, method: str,
             data: Dict = None) -> requests.Response:
        return self._session.request(
            method=method,
            url=f'{self._BASE_URL}{path}',
            data=data,
            timeout=10,
        )
