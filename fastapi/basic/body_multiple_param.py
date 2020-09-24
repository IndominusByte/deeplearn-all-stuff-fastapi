from fastapi import FastAPI, Body
from pydantic import BaseModel, StrictFloat
from typing import Optional

class MyConfig(BaseModel):
    class Config:
        anystr_strip_whitespace = True
        min_anystr_length = 1

class Item(MyConfig):
    name: str
    price: StrictFloat
    description: Optional[str] = None
    tax: Optional[StrictFloat] = None

class User(MyConfig):
    username: str
    full_name: Optional[str] = None


app = FastAPI()

# @app.put('/items/{item_id}')
# def update_item(item_id: int, item: Item, user: User):
#     return {"item_id": item_id, "item": item, "user": user}

# Singular values in body
@app.put('/items/{item_id}')
def update_item(
    item_id: int,
    item: Item,
    user: User,
    importance: int = Body(...),
    q: Optional[str] = None
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results
