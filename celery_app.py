from celery import Celery

import config
from vote.vote_pack import VotePack

celery_app = Celery('main', broker=config.CELERY_BROKER,
                    backend=config.CELERY_BROKER)

celery_app.conf.task_default_queue = 'chartova'


@celery_app.task(acks_late=True)
def vote_pack(**kwargs) -> None:
    VotePack().run(track_id=kwargs['track_id'])
