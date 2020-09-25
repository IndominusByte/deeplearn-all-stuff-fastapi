from fastapi import FastAPI, Cookie
from typing import Optional

app = FastAPI()

@app.get("/items/")
async def read_items(ads_id: Optional[str] = Cookie(None)):
    return {"ads_id": ads_id}
