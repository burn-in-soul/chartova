import random
import time

import requests
from fake_useragent import UserAgent

from system_service.pystemd_service import SystemdService
from vote.one_vote import Vote
from vote.parser import Parser


class Voter:
    def __init__(self) -> None:
        self._session = requests.Session()
        self._prepare_data()

    def vote_pack(self, track_id: int) -> None:
        one_vote = Vote(session=self._session,
                        headers=self._headers)
        for i in range(3):
            one_vote.run(track_id=track_id,
                         iteration_id=self.iteration_id)
            time.sleep(random.uniform(3, 6))

        SystemdService().restart('tor.service')

    def _prepare_data(self) -> None:
        self._headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': UserAgent().random
        }
        response = self._session.get('https://www.nashe.ru/chartova/')
        parser = Parser(response.content)
        self._headers['X-CSRF-TOKEN'] = parser.get_csrf()
        self.iteration_id = parser.get_iteration_id()
