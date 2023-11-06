from logger import logging
import random
import time

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class Voter:
    def __init__(self) -> None:
        self._session = requests.Session()
        self._headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': UserAgent().random
        }
        self._prepare_data()

    def vote_pack(self, track_id: int) -> None:
        for i in range(3):
            self._vote(track_id=track_id)
            time.sleep(random.uniform(3, 6))

    def _vote(self, track_id: int) -> None:
        response = self._session.post(
            url='https://www.nashe.ru/chartova/vote',
            headers=self._headers,
            data={'track_id': '1017', 'iteration_id': self.iteration_id}
        )
        if response.status_code == 200:
            logging.info(f'Проголосовал: {track_id}')
        else:
            logging.error(response.text)

    def _prepare_data(self) -> None:
        response = self._session.get('https://www.nashe.ru/chartova/')
        soup = BeautifulSoup(response.content, 'html.parser')
        csrf = soup.find(name='meta', attrs={'name': 'csrf-token'})['content']
        self._headers['X-CSRF-TOKEN'] = csrf
        self.iteration_id = soup.find(
            name='div',
            attrs={'class': 'chartova__items'}
        )['data-iteration']
