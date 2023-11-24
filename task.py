from celery import Celery

app = Celery(broker='redis://127.0.0.1:6379/0')

@app.task(bind = True)
def create_playlist(self, name, gender):
    
