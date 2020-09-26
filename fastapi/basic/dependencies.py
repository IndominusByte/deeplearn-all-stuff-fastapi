from fastapi import FastAPI, Depends, Cookie, Header, HTTPException
from typing import Optional

app = FastAPI()

# dependable
async def common_paremeters(q: Optional[str] = None, skip: Optional[int] = 0, limit: Optional[int] = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.get('/items')
async def items(commons: dict = Depends(common_paremeters)):
    return commons

# Classes as dependencies
class CommonQueryParam:
    def __init__(self, q: Optional[str] = None, skip: Optional[int] = 0, limit: Optional[int] = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


# Shortcut
@app.get('/items_2')
# async def items_2(commons: CommonQueryParam = Depends(CommonQueryParam)):
async def items_2(commons: CommonQueryParam = Depends()):
    print(id(commons))
    return commons

# Sub-dependencies
async def query_extractor(q: Optional[str] = None):
    return q

async def query_or_cookie_extractor(q: query_extractor = Depends(), last_query: Optional[str] = Cookie(None)):
    if not q:
        return last_query
    return q

@app.get('/items_3')
async def items_3(commons: query_or_cookie_extractor = Depends()):
    return commons

# Dependencies in path operation decorators
"""
In some cases you don't really need the return value of a dependency inside your path operation function.

Or the dependency doesn't return a value.

But you still need it to be executed/solved.

For those cases, instead of declaring a path operation function parameter with Depends, you can add a list of dependencies to the path operation decorator.
"""
async def verify_token(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

async def verify_key(x_key: str = Header(...)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key

@app.get('/items_4', dependencies=[Depends(verify_token), Depends(verify_key)])
async def items_4():
    return [{"item": "Foo"}, {"item": "Bar"}]
