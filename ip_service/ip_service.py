import requests


class IpService:

    def __init__(self, session: requests.Session) -> None:
        self._session = session

    def check(self) -> str:
        return self._session.get(
            url='https://ifconfig.me/ip',
            headers={'Content-Type': 'application/json'}).text
