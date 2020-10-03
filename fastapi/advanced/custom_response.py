from fastapi import FastAPI
from fastapi.responses import (
    ORJSONResponse,
    HTMLResponse,
    RedirectResponse,
    StreamingResponse,
    FileResponse
)

# When creating a FastAPI class instance or an APIRouter you can specify which response class to use by default.
app = FastAPI(default_response_class=ORJSONResponse)

# Use ORJSONResponse
"""
For example, if you are squeezing performance, you can install and use orjson and set the response to be ORJSONResponse.
Import the Response class (sub-class) you want to use and declare it in the path operation decorator.
"""
@app.get('/orjson', response_class=ORJSONResponse)
async def read_orjson():
    return [{"item_id": "Foo"}]

# HTML Response
@app.get('/html', response_class=HTMLResponse)
async def read_html():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """

# RedirectResponse
@app.get('/redirect')
async def redirect():
    return RedirectResponse("https://mentimun-mentah.tech/")

# StreamingResponse
@app.get('/streaming')
async def streaming():
    file = open('video/automatch.mp4',mode='rb')
    return StreamingResponse(file, media_type='video/mp4')

# FileResponse
"""
Asynchronously streams a file as the response.

Takes a different set of arguments to instantiate than the other response types:

- path - The filepath to the file to stream.
- headers - Any custom headers to include, as a dictionary.
- media_type - A string giving the media type. If unset, the filename or path will be used to infer a media type.
- filename - If set, this will be included in the response Content-Disposition.

File responses will include appropriate Content-Length, Last-Modified and ETag headers.
"""
@app.get('/file')
async def file():
    return FileResponse('video/automatch.mp4')
