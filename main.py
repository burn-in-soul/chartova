import datetime
import sys

from dotenv import load_dotenv

from create_task import create_tasks
from intervals.interval import Interval

load_dotenv()


def main(track_id: int, vote_count: int) -> None:
    now = datetime.datetime.now()
    intervals = Interval(vote_count).generate(now.hour)
    create_tasks(track_id, intervals)


if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
