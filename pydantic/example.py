from datetime import datetime
from pydantic import BaseModel, ValidationError
from typing import List, Optional


class User(BaseModel):
    id: int
    signup_ts: datetime
    friends: List[int]
    name: Optional[str] = 'john doe'


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}

user = User(**external_data)
print(user.id)
# >123
print(repr(user.signup_ts))
# > datetime.datetime(2019, 6, 1, 12, 22)
print(user.friends)
# > [1, 2, 3]
print(user.dict())
print()
"""
{
    'id': 123,
    'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
    'friends': [1, 2, 3],
    'name': 'John Doe',
}
"""

try:
    User(signup_ts='broken', friends=[1, 2, 'not number'])
except ValidationError as err:
    print(err.json())
