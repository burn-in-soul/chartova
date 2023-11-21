from bs4 import BeautifulSoup
from requests.structures import CaseInsensitiveDict


class Parser:
    """Парсер данных с сайта nashe"""
    
    def __init__(self, content: bytes) -> None:
        self.soup = BeautifulSoup(content, 'html.parser')

    def get_iteration_id(self) -> int:
        return int(self.soup.find(
            name='div',
            attrs={'class': 'chartova__items'}
        )['data-iteration'])

    def get_csrf(self) -> str:
        return self.soup.find(name='meta',
                              attrs={'name': 'csrf-token'})['content']

    @staticmethod
    def get_cookie(headers: CaseInsensitiveDict) -> str:
        cookie = headers['Set-Cookie']
        xsrf_token = cookie.split('XSRF-TOKEN=')[1].split(' ')[0]
        laravel_session = cookie.split('laravel_session=')[1].split(' ')[0]
        weborama_user_id = cookie.split('_weborama_user_id=')[1].split(' ')[0]
        return (f'_weborama_user_id={weborama_user_id} '
                f'XSRF-TOKEN={xsrf_token} '
                f'laravel_session={laravel_session}')
