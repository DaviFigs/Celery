from celery import shared_task
import time
from . import pillow as pl
from . import email as ems

@shared_task
def test():
    time.sleep(5)
    return {'test':'this is a test'}


@shared_task
def send_invite(name,email):
    try:
        image = pl.configure_image(name)
        ems.send_mail(email, name)
        return {'Success':'Email was sent'}

    except Exception as e:
        return {'Error',f'{e}'}

