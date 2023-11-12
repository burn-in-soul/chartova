from typing import Dict

import requests

import config
from logger import logging


class Vote:
    def __init__(self, session: requests.Session, headers: Dict) -> None:
        self._headers = headers
        self._session = session
        self._session.proxies = {'http': config.TOR_PROXY,
                                 'https': config.TOR_PROXY}

    def run(self, track_id: int, iteration_id: int) -> None:
        response = self._session.post(
            url='https://www.nashe.ru/chartova/vote',
            headers=self._headers,
            data={'track_id': track_id, 'iteration_id': iteration_id}
        )
        if response.status_code == 200:
            logging.info(f'Проголосовал: {track_id}')
        else:
            logging.error(response.text)
