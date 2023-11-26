from celery import Celery
from time import sleep

app = Celery(broker='redis://127.0.0.1:6379/0')

@app.task(bind = True)
def home():
    sleep(3)
    return 'Hello world'