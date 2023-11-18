import requests

from request_utils.chartova_request import ChartovaRequest


class Vote:
    def __init__(self, session: requests.Session) -> None:
        self._session = session

    def run(self, track_id: int, iteration_id: int) -> None:
        response = ChartovaRequest(session=self._session).make(
            method='POST',
            path='vote/',
            data={'track_id': track_id, 'iteration_id': iteration_id},
        )
        if response.status_code != 200:
            raise ConnectionError(response.text)
