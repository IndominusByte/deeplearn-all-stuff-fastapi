"""
The .json() method will serialise a model to JSON. Typically, .json() in turn calls .dict() and serialises its result. (For models with a custom root type, after calling .dict(), only the value for the __root__ key is serialised)

Arguments:

- include: fields to include in the returned dictionary; see below
- exclude: fields to exclude from the returned dictionary; see below
- by_alias: whether field aliases should be used as keys in the returned dictionary; default False
- exclude_unset: whether fields which were not set when creating the model and have their default values should be excluded from the returned dictionary; default False. Prior to v1.0, exclude_unset was known as skip_defaults; use of skip_defaults is now deprecated
- exclude_defaults: whether fields which are equal to their default values (whether set or otherwise) should be excluded from the returned dictionary; default False
- exclude_none: whether fields which are equal to None should be excluded from the returned dictionary; default False
- encoder: a custom encoder function passed to the default argument of json.dumps(); defaults to a custom encoder designed to take care of all common types
- **dumps_kwargs: any other keyword arguments are passed to json.dumps(), e.g. indent.
"""
from pydantic import BaseModel
from datetime import datetime

class BarModel(BaseModel):
    whatever: int

class FooBarModel(BaseModel):
    foo: datetime
    bar: BarModel


m = FooBarModel(foo=datetime(2032, 6, 1, 12, 13, 14),bar={'whatever':123})
print(m.json())
# > {"foo": "2032-06-01T12:13:14", "bar": {"whatever": 123}}
