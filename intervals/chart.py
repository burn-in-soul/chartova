import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import config


class Chart:
    """График голосов в день"""

    def __init__(self, vote_count: int) -> None:
        self.vote_count = vote_count

    def create(self) -> None:
        data = {
            'Время': [i for i in range(24)],
            'Голоса': [ratio * self.vote_count
                       for ratio in config.HOURS.values()]
        }
        df = pd.DataFrame(data)
        plt.xticks(np.arange(0, 24, 1.0))
        plt.xlim(0, 23)
        plt.plot(df['Время'], df['Голоса'])
        plt.title('Распределение голосов')
        plt.xlabel('Время')
        plt.ylabel('Голоса')
        plt.show()
