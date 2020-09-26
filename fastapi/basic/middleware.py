import time
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def add_ip_address(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(round(process_time,2))
    return response


@app.get('/time')
def get_time():
    return "asdasdasdasd"
