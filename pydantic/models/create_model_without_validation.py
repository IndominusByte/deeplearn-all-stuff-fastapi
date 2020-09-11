"""
pydantic also provides the construct() method which allows models to be created without validation
this can be useful when data has already been validated or comes from a trusted source
and you want to create a model as efficiently as possible
(construct() is generally around 30x faster than creating a model with full validation).
"""
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    age: int
    name: Optional[str] = 'John Doe'


original_user = User(id=123, age=32)

new_user = User.construct(**original_user.dict())
print(new_user)
