import aplication as ap
from fastapi import FastAPI

app = FastAPI()


@app.post('/sum')
def sum_numbs(num1:int, num2:int):
    final = ap.sum_numbs(num1, num2)
    return {'result': final}