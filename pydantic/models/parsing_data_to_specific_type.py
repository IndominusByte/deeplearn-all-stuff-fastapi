from pydantic import BaseModel, parse_obj_as
from typing import List

"""
Pydantic includes a standalone utility function parse_obj_as that can be used
to apply the parsing logic used to populate pydantic models in a more ad-hoc way.
This function behaves similarly to BaseModel.parse_obj, but works with arbitrary pydantic-compatible types.

This is especially useful when you want to parse results into a type that is not a direct subclass of BaseModel.
For example:
"""
class Item(BaseModel):
    id: int
    name: str


# `item_data` could come from an API call, eg., via something like:
# item_data = requests.get('https://my-api.com/items').json()
item_data = [{'id': 1, 'name': 'My Item'}]

items = parse_obj_as(List[Item], item_data)
print(items)
# > [Item(id=1, name='My Item')]
