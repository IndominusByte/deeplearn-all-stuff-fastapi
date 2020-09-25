from fastapi import FastAPI

app = FastAPI()

@app.post('/items', status_code=201)
def create_item(name: str):
    return {'name': name}
