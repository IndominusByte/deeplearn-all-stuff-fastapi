"""
By default, FastAPI will return the responses using a JSONResponse, putting the content you return from your path operation inside of that JSONResponse.
"""
# Warning
"""
When you return a Response directly It won't be serialized with a model, etc.
"""
# OpenAPI and API docs
"""
If you return additional status codes and responses directly, they won't be included in the OpenAPI schema (the API docs), because FastAPI doesn't have a way to know beforehand what you are going to return.
"""
