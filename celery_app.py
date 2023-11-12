from celery import Celery

import config
from vote.voter import Voter

celery_app = Celery('main', broker=config.CELERY_BROKER)

celery_app.conf.task_default_queue = 'chartova'


@celery_app.task
def vote_pack(**kwargs) -> None:
    Voter().vote_pack(track_id=kwargs['track_id'])
