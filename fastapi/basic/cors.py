from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

"""
The following arguments are supported:

- allow_origins - A list of origins that should be permitted to make cross-origin requests. E.g. ['https://example.org', 'https://www.example.org']. You can use ['*'] to allow any origin.

- allow_origin_regex - A regex string to match against origins that should be permitted to make cross-origin requests. eg. 'https://.*.example.org'.

- allow_methods - A list of HTTP methods that should be allowed for cross-origin requests. Defaults to ['GET']. You can use ['*'] to allow all standard methods.

- allow_headers - A list of HTTP request headers that should be supported for cross-origin requests. Defaults to []. You can use ['*'] to allow all headers. The Accept, Accept-Language, Content-Language and Content-Type headers are always allowed for CORS requests.

- allow_credentials - Indicate that cookies should be supported for cross-origin requests. Defaults to False.
- expose_headers - Indicate any response headers that should be made accessible to the browser. Defaults to [].
- max_age - Sets a maximum time in seconds for browsers to cache CORS responses. Defaults to 600.
"""
origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Hello World"}
