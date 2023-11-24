from fastapi import FastAPI

app =  FastAPI()

@app.get('/home')
def return_nothing():
    return {'message':'Nothing'}