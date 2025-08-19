import random

from fastapi import FastAPI

app = FastAPI()

#127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Hello World"}


#127.0.0.1:8000/teste
@app.get("/teste")
async def functest():
    return {"teste": True, "Worked": random.randint(0, 1000)}