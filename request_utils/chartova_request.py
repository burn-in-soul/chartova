from typing import Dict

import requests


class ChartovaRequest:
    """Запрос в chartova"""

    _BASE_URL = 'https://www.nashe.ru/chartova/'

    def __init__(self, session: requests.Session) -> None:
        self._session = session

    def make(self, path: str, method: str,
             data: Dict = None) -> requests.Response:
        response = self._session.request(
            method=method,
            url=f'{self._BASE_URL}{path}',
            data=data,
            timeout=10,
        )
        if response.status_code != 200:
            raise ConnectionError(response.text)
        return response
