from typing import Dict

import requests

from logger import logging


class Vote:
    def __init__(self, session: requests.Session, headers: Dict) -> None:
        self._headers = headers
        self._session = session

    def run(self, track_id: int, iteration_id: int) -> None:
        response = self._session.post(
            url='https://www.nashe.ru/chartova/vote',
            headers=self._headers,
            data={'track_id': track_id, 'iteration_id': iteration_id},
            timeout=10,
        )
        if response.status_code == 200:
            print(f'Проголосовал: {track_id}')
        else:
            print(response.text)
