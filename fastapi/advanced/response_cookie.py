from fastapi import FastAPI, Response

app = FastAPI()

@app.get('/cookie')
async def get_cookie(res: Response):
    res.set_cookie(key='name',value='oman')
    return {"message": "Come to the dark side, we have cookies"}
