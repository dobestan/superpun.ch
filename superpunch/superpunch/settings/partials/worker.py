import os

from celery.schedules import crontab


BROKER_URL = os.environ.get(
    'BROKER_URL',
    'redis://localhost:6379/0',
)


CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


CELERYBEAT_SCHEDULE = {
    'Tidbits | Update Provider Feeds': {
        'task': 'tidbits.tasks.feed.UpdateProviderFeedTask',
        'schedule': crontab(
            minute='00',
        )
    },
}


CELERY_TIMEZONE = 'Asia/Seoul'


# Celery Custom Settings
# http://celery.readthedocs.org/en/latest/configuration.html

CELERY_APP = "superpunch.celery:app"

CELERY_IGNORE_RESULT = True
