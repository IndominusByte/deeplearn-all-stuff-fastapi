from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get('/items/{item_id}')
def read_items(
    item_id: int = Path(..., gt=0, title='The ID of the item to get'),
    q: str = Query(None, alias='item-query')
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
