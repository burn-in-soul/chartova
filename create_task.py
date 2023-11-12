from datetime import datetime, timedelta
from typing import List

from celery import group
from pytz import timezone

from celery_app import vote_pack, test_task

msc_tz = timezone('Europe/Moscow')


def create_tasks(track_id: int, intervals: List[float]) -> None:
    countdown = 0
    task_group = []
    for interval in intervals:
        task_group.append(
            vote_pack.s(
                eta=msc_tz.localize(datetime.now()) + timedelta(countdown),
                kwargs={'track_id': track_id},
                queue='chartova'
            ))
        countdown += interval
    job = group(task_group)
    job.apply_async()