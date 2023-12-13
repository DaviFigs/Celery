from celery import shared_task
import time
from . import pillow as pl
from core.settings import SendEmail

@shared_task
def test():
    time.sleep(5)
    return {'test':'this is a test'}


@shared_task
def send_invite(name, cpf,email):
    try:
        image = pl.configure_image(name, cpf)
        sender = SendEmail()
        sender.send_email(email, name, image)
        return {'success':'email was send'}
    except:
        return {'error':f'Cannot send email'}


