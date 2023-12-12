from celery import shared_task
import time

@shared_task
def test():
    time.sleep(5)
    return {'test':'this is a test'}