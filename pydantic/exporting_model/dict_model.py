"""
This is the primary way of converting a model to a dictionary. Sub-models will be recursively converted to dictionaries.

Arguments:

- include: fields to include in the returned dictionary; see below
- exclude: fields to exclude from the returned dictionary; see below
- by_alias: whether field aliases should be used as keys in the returned dictionary; default False
- exclude_unset: whether fields which were not explicitly set when creating the model should be excluded from the returned dictionary; default False. Prior to v1.0, exclude_unset was known as skip_defaults; use of skip_defaults is now deprecated
- exclude_defaults: whether fields which are equal to their default values (whether set or otherwise) should be excluded from the returned dictionary; default False
- exclude_none: whether fields which are equal to None should be excluded from the returned dictionary; default False
"""
from pydantic import BaseModel

class BarModel(BaseModel):
    whatever: int

class FooBarModel(BaseModel):
    banana: float
    foo: str
    bar: BarModel


m = FooBarModel(banana=3.14, foo='hello', bar={'whatever': 123})
# returns a dictionary:
print(m.dict())
"""
{
    'banana': 3.14,
    'foo': 'hello',
    'bar': {'whatever': 123},
}
"""
print(m.dict(include={'foo', 'bar'}))
# > {'foo': 'hello', 'bar': {'whatever': 123}}
print(m.dict(exclude={'foo', 'bar'}))
# > {'banana': 3.14}

for name,value in m:
    print(name,value)
