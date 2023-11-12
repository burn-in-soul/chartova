import random
import time

import requests
import stem.control
import stem.util
from fake_useragent import UserAgent

import config
from ip_service.ip_service import IpService
from vote.one_vote import Vote
from vote.parser import Parser

stem.util.log.get_logger().propagate = False


class Voter:
    def __init__(self) -> None:
        self._session = requests.Session()
        self._session.proxies = {'http': config.TOR_PROXY,
                                 'https': config.TOR_PROXY}
        self._prepare_data()

    def vote_pack(self, track_id: int) -> None:
        print('run task')
        with stem.control.Controller.from_port(
                address=config.TOR_HOST,
                port=config.TOR_PORT) as controller:
            controller.authenticate(password=config.TOR_PASSWORD)
            print('get controller')
            one_vote = Vote(session=self._session, headers=self._headers)
            ip = IpService(session=self._session).check()
            print(f'Start with ip: {ip}')
            for i in range(3):
                one_vote.run(track_id=track_id,
                             iteration_id=self.iteration_id)
                time.sleep(random.uniform(2, 5))
            controller.signal(stem.Signal.HUP)

    def _prepare_data(self) -> None:
        self._headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': UserAgent().random
        }
        response = self._session.get('https://www.nashe.ru/chartova/',
                                     proxies={}, timeout=10)
        parser = Parser(response.content)
        self._headers['X-CSRF-TOKEN'] = parser.get_csrf()
        self.iteration_id = parser.get_iteration_id()
