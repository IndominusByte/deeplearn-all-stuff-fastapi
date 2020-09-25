"""
When raising an HTTPException, you can pass any value that can be converted to JSON as the parameter detail, not only str.
You could pass a dict, a list, etc.
They are handled automatically by FastAPI and converted to JSON.
"""
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import ORJSONResponse

app = FastAPI()

@app.get('/items/{item_id}')
def read_item(item_id: str):
    if item_id not in {"foo": "The Foo Wrestlers"}:
        raise HTTPException(
            status_code=404,
            detail={'message':'lol'},
            # headers={"X-Error": "There goes my error"},
        )
    return {"foo": "The Foo Wrestlers"}

# Install custom exception handlers
class UnicornException(Exception):
    def __init__(self, message: str):
        # super().__init__(message)
        self.message = message

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return ORJSONResponse(
        status_code=404,
        content={'message': f"Oops! {exc.message} did something. There goes a rainbow..."}
    )

@app.get("/unicorn/{name}")
def read_unicorn(name: str):
    if name == 'yolo':
        raise UnicornException(message=name)
    return {"unicorn_name": name}
