from typing import List
from celery_app import vote_pack, test_task


def create_tasks(track_id: int, intervals: List[float]) -> None:
    countdown = 0
    for interval in intervals:
        vote_pack.apply_async(countdown=countdown,
                              kwargs={'track_id': track_id})
        countdown += interval
