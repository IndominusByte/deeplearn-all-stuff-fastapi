"""
Note that in this case, we are declaring a path parameter beside the request parameter.

So, the path parameter will be extracted, validated, converted to the specified type and annotated with OpenAPI.

The same way, you can declare any other parameter as normally, and additionally, get the Request too.
"""
from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/items/{item_id}')
def read_root(item_id: str, request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "item_id": item_id}
