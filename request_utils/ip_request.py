import requests


class IpRequest:
    _BASE_URL = 'http://httpbin.org/ip'

    def __init__(self, session: requests.Session) -> None:
        self._session = session

    def make(self) -> requests.Response:
        return self._session.get(
            url=self._BASE_URL,
            headers={'Content-Type': 'application/json'},
        )
