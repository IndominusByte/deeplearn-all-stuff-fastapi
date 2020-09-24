from fastapi import FastAPI
from pydantic import BaseModel, StrictFloat
from typing import Optional

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: StrictFloat
    tax: Optional[float] = None

    class Config:
        anystr_strip_whitespace = True
        min_anystr_length = 1


app = FastAPI()

@app.post('/items')
def create_items(item: Item):
    return item.dict()


# Request body + path parameters
"""
You can declare path parameters and body requests at the same time.

FastAPI will recognize that the function parameters that match path parameters should be taken from the path, and that function parameters that are declared to be Pydantic models should be taken from the request body.
"""
# @app.put('/items/{item_id}')
# def update_items(item_id: int, item:Item):
#     return {"item_id": item_id, **item.dict()}

"""
The function parameters will be recognized as follows:

If the parameter is also declared in the path, it will be used as a path parameter.
If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter.
If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body.
"""
# Request body + path + query parameters
@app.put('/items/{item_id}')
def update_items(item:Item, item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q,**item.dict()}
