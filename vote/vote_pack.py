import random
import time

import requests
from fake_useragent import UserAgent

import config
from ip_service.ip_service import IpService
from request_utils.chartova_request import ChartovaRequest
from tor_service.tor_controller import TorController
from vote.parser import Parser
from vote.vote import Vote


class VotePack:
    """Пакет из 3 голосов от 1 пользователя"""

    def __init__(self) -> None:
        self._session = requests.Session()
        self._session.headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': UserAgent().random
        }
        self._session.proxies = {'http': config.TOR_PROXY,
                                 'https': config.TOR_PROXY}

    def run(self, track_id: int) -> None:
        with TorController() as controller:
            self._prepare_data()
            one_vote = Vote(session=self._session)
            for i in range(3):
                one_vote.run(track_id=track_id,
                             iteration_id=self.iteration_id)
                if i < 2:
                    time.sleep(random.uniform(2, 5))
            ip = IpService(session=self._session).check()
            print(f'3 votes to {track_id} with ip: {ip}')
            controller.reload()

    def _prepare_data(self) -> None:
        response = ChartovaRequest(self._session).make(
            path='',
            method='GET',
        )
        parser = Parser(response.content)
        self._session.headers['Cookie'] = parser.get_cookie(response.headers)
        self._session.headers['X-Csrf-Token'] = parser.get_csrf()
        self.iteration_id = parser.get_iteration_id()
