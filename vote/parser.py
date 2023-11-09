from bs4 import BeautifulSoup


class Parser:

    def __init__(self, content: bytes) -> None:
        self.content = content

    def get_iteration_id(self) -> int:
        soup = BeautifulSoup(self.content, 'html.parser')
        return int(soup.find(
            name='div',
            attrs={'class': 'chartova__items'}
        )['data-iteration'])

    def get_csrf(self) -> str:
        soup = BeautifulSoup(self.content, 'html.parser')
        return soup.find(name='meta', attrs={'name': 'csrf-token'})['content']
