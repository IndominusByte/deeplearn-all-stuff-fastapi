from fastapi import FastAPI, Header, HTTPException, Depends
from routers import items, users

app = FastAPI()

async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

app.include_router(users.router,tags=['users'])
"""
They will be marked with a list of tags that contain a single string "items".
The path operation that declared a "custom" tag will have both tags, items and custom.
"""
app.include_router(
    items.router,
    prefix="/items",
    tags=['items'],
    dependencies=[Depends(get_token_header)]
)
