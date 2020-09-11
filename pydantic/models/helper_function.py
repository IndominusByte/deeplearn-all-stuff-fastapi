"""
Pydantic provides three classmethod helper functions on models for parsing data:

parse_obj: this is very similar to the __init__ method of the model,
except it takes a dict rather than keyword arguments.
If the object passed is not a dict a ValidationError will be raised.

parse_raw: this takes a str or bytes and parses it as json, then passes the result to parse_obj.
Parsing pickle data is also supported by setting the content_type argument appropriately.

parse_file: this reads a file and passes the contents to parse_raw.
If content_type is omitted, it is inferred from the file's extension.
"""
from pydantic import BaseModel, ValidationError
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: int
    name: Optional[str] = 'John Doe'
    signup_ts: Optional[datetime] = None


m = User.parse_obj({'id': 123, 'name': 'James'})
print(m)
print()
# > id=123 signup_ts=None name='James'

try:
    User.parse_obj(['not', 'a', 'dict'])
except ValidationError as e:
    print(e)
    print()

"""
1 validation error for User
__root__
  User expected dict not list (type=type_error)
"""

# assumes json as no content type passed
m = User.parse_raw('{"id": 123, "name": "James"}')
print(m)
# > id=123 signup_ts=None name='James'
