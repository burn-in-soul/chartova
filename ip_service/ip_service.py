import requests

from request_utils.ip_request import IpRequest


class IpService:

    def __init__(self, session: requests.Session) -> None:
        self._session = session

    def check(self) -> str:
        return IpRequest(self._session).make().json()['origin']
