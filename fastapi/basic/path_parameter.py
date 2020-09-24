from fastapi import FastAPI
from typing import Literal

app = FastAPI()

@app.get('/item/{item_id}')
def item(item_id: int):
    return {"item_id": item_id}

@app.get('/user/{user_name}')
def user(user_name: Literal['oman','pradipta','dewantara']):
    if user_name == 'oman':
        return {"user_name": user_name,"message": "Deep Learning FTW!"}
    if user_name == 'pradipta':
        return {"user_name": user_name,"message": "LeCNN all the images"}

    return {"user_name": user_name,"message": "Have some residuals"}
