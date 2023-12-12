from PIL import Image
from celery import shared_task
import time

@shared_task
def test():
    time.sleep(5)
    return {'test':'this is a test'}




@shared_task
def configure_image():
    pass

