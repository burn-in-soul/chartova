import random
import time

import requests
import stem.control
import stem.util
from fake_useragent import UserAgent

import config
from ip_service.ip_service import IpService
from request_utils.chartova_request import ChartovaRequest
from vote.vote import Vote
from vote.parser import Parser

stem.util.log.get_logger().propagate = False


class VotePack:
    def __init__(self) -> None:
        self._session = requests.Session()
        self._session.headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': UserAgent().random
        }
        self._session.proxies = {'http': config.TOR_PROXY,
                                 'https': config.TOR_PROXY}

    def run(self, track_id: int) -> None:
        with stem.control.Controller.from_port(
                address=config.TOR_HOST,
                port=config.TOR_CONTROL_PORT) as controller:
            controller.authenticate(password=config.TOR_PASSWORD)
            self._prepare_data()
            one_vote = Vote(session=self._session)
            for i in range(3):
                one_vote.run(track_id=track_id,
                             iteration_id=self.iteration_id)
                if i < 2:
                    time.sleep(random.uniform(2, 5))
            ip = IpService(session=self._session).check()
            print(f'3 votes to {track_id} with ip: {ip}')
            controller.signal(stem.Signal.NEWNYM)

    def _prepare_data(self) -> None:
        response = ChartovaRequest(self._session).make(
            path='',
            method='GET',
        )
        parser = Parser(response.content)
        self._session.headers = response.headers
        self._session.headers['X-CSRF-TOKEN'] = parser.get_csrf()
        self.iteration_id = parser.get_iteration_id()
