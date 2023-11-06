import datetime

from dotenv import load_dotenv

import config
from create_task import create_tasks
from intervals.interval import Interval

load_dotenv()


def main() -> None:
    now = datetime.datetime.now()
    intervals = Interval(config.VOTE_COUNT).generate(now.hour)
    create_tasks(config.TRACK_ID, intervals)


if __name__ == '__main__':
    main()
