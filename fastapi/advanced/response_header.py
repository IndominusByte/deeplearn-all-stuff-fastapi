from fastapi import FastAPI, Response

app = FastAPI()

@app.get('/header')
async def header(res: Response):
    res.headers["X-Cat-Dog"] = "alone in the world"
    return {"message": "Hello World"}
