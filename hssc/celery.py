# from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hssc.settings')

app = Celery('hssc')
# app = Celery('hssc', backend='redis://localhost', broker='pyamqp://')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'From celery.py, Request: {self.request!r}')