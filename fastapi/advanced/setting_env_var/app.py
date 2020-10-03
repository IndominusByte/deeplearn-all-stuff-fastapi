from fastapi import FastAPI, Depends
from functools import lru_cache
from config import Settings

app = FastAPI()

@lru_cache
def get_settings():
    return Settings()

@app.get('/info')
async def info(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "environment": settings.environment,
        "token_expired": settings.token_expired
    }
