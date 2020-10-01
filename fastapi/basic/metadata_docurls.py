from fastapi import FastAPI

# Title, description, and version
"""
You can set the:

- Title: used as your API's title/name, in OpenAPI and the automatic API docs UIs.
- Description: the description of your API, in OpenAPI and the automatic API docs UIs.
- Version: the version of your API, e.g. v2 or 2.5.0.
"""
# app = FastAPI(
#     title="My Super Project",
#     description="This is a very fancy project, with auto docs for the API and everything",
#     version="2.5.0",
# )

# OpenAPI URL
"""
By default, the OpenAPI schema is served at /openapi.json.
But you can configure it with the parameter openapi_url.
For example, to set it to be served at /api/v1/openapi.json:

If you want to disable the OpenAPI schema completely you can set openapi_url=None, that will also disable the documentation user interfaces that use it.
"""
# app = FastAPI(openapi_url="/api/v1/openapi.json")
# app = FastAPI(openapi_url=None)

# Docs URLs
"""
You can configure the two documentation user interfaces included:

Swagger UI: served at /docs.
- You can set its URL with the parameter docs_url.
- You can disable it by setting docs_url=None.

ReDoc: served at /redoc.
- You can set its URL with the parameter redoc_url.
- You can disable it by setting redoc_url=None.
"""
app = FastAPI(docs_url="/documentation", redoc_url=None)


@app.get("/items/")
async def read_items():
    return [{"name": "Foo"}]
