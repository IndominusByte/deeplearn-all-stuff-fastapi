from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount('/static', StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# NOTE: Notice that you have to pass the request as part of the key-value pairs in the context for Jinja2. So, you also have to declare it in your path operation.

@app.get('/message/{name}', response_class=HTMLResponse)
def main(name: str, request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": name})
