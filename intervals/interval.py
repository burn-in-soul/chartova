from logger import logging
import random
from typing import List

import config


class Interval:

    def __init__(self, vote_count: int) -> None:
        self.vote_count = vote_count

    def generate(self, hour: int) -> List[float]:
        hour_vote_count = self._get_hour_count(hour)
        try:
            default_interval = 3600 / hour_vote_count
        except ZeroDivisionError:
            logging.error('Менее 1 голоса в час')
            return []
        return [
            default_interval + random.uniform(-config.RANDOM_INTERVAL,
                                              config.RANDOM_INTERVAL)
            for _ in range(hour_vote_count)
        ]

    @staticmethod
    def sum_intervals() -> float:
        return sum(config.HOURS.values())

    def _get_hour_count(self, hour: int) -> int:
        return int(config.HOURS[hour] * self.vote_count)
