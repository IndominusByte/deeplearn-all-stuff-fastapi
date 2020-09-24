from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/pertambahan')
def pertambahan(value_1: int, value_2: int):
    return {"hasil": value_1 + value_2}

# optional parameter
@app.get('/items')
def items(q: Optional[str] = None):
    return {"q": q}

# Multiple path and query parameters
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
