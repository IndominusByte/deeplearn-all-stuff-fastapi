from fastapi import FastAPI

app = FastAPI()

# Tags
# Summary and description
# Response description
@app.get(
    '/items',
    tags=['items'],
    summary="Create an item",
    description="Create an item with all the information, name, description, price, tax and a set of unique tags",
    response_description="The created item"
)
def items():
    return "items"

# Deprecate a path operation
@app.get('/items/{item_id}', tags=['items'], deprecated=True)
def items_get_id(item_id: int):
    return item_id


# Description from docstring
"""
As descriptions tend to be long and cover multiple lines, you can declare the path operation description in the function docstring and FastAPI will read it from there.

You can write Markdown in the docstring, it will be interpreted and displayed correctly (taking into account docstring indentation).
"""
@app.get('/users', tags=['users'], summary="Get all users")
def read_user():
    """
    Create an user with all the information:
    -----------
    Numbered list:

    1. lather
    2. rinse
    3. repeat
    """
    return "users"
