import json

import requests


class IpService:

    def __init__(self, session: requests.Session) -> None:
        self._session = session

    def check(self) -> str:
        return json.loads(self._session.get(
            url='http://httpbin.org/ip',
            headers={'Content-Type': 'application/json'}).content)['origin']
