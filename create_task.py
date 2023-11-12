from datetime import datetime, timedelta
from typing import List

from pytz import timezone

from celery_app import vote_pack, test_task

msc_tz = timezone('Europe/Moscow')


def create_tasks(track_id: int, intervals: List[float]) -> None:
    countdown = 0
    for interval in intervals:
        vote_pack.apply_async(
            eta=msc_tz.localize(datetime.now()) + timedelta(seconds=countdown),
            kwargs={'track_id': track_id},
            queue='chartova'
        )
        print(msc_tz.localize(datetime.now()) + timedelta(seconds=countdown))
        countdown += interval
