"""
The dict, json, and copy methods support include and exclude arguments which can either be sets or dictionaries. This allows nested selection of which fields to export:
"""
from pydantic import BaseModel, SecretStr

class User(BaseModel):
    id: int
    username: str
    password: SecretStr

class Transaction(BaseModel):
    id: str
    user: User
    value: int


t = Transaction(
    id='1234567890',
    user=User(
        id=42,
        username='JohnDoe',
        password='hashedpassword'
    ),
    value=9876543210,
)
"""
The ellipsis (...) indicates that we want to exclude or include an entire key, just as if we included it in a set. Of course, the same can be done at any depth level.
"""
# using a set:
print(t.json(exclude={'user','value'}))
# > {'id': '1234567890'}

# using a dict:
print(t.json(exclude={'user':{'username','password'},'value': ...}))
# > {'id': '1234567890', 'user': {'id': 42}}
print(t.json(include={'id': ...,'user':{'id'}}))
# > {'id': '1234567890', 'user': {'id': 42}}
