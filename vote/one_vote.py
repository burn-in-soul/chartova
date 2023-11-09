from typing import Dict

import requests

from logger import logging


class Vote:
    def __init__(self, headers: Dict) -> None:
        self._headers = headers

    def vote(self, track_id: int, iteration_id: int) -> None:
        response = requests.post(
            url='https://www.nashe.ru/chartova/vote',
            headers=self._headers,
            data={'track_id': track_id, 'iteration_id': iteration_id}
        )
        if response.status_code == 200:
            logging.info(f'Проголосовал: {track_id}')
        else:
            logging.error(response.text)
