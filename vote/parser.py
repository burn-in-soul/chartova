from bs4 import BeautifulSoup


class Parser:

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
