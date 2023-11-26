from fastapi import FastAPI
import task as tk

app =  FastAPI()

@app.get('/home')
def home():
    msg = tk.home.delay()
    return msg