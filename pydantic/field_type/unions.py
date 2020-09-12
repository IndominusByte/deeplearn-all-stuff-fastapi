"""
The Union type allows a model attribute to accept different types, e.g.:
"""
from pydantic import BaseModel
from uuid import UUID
from typing import Union

class User(BaseModel):
    id: Union[int, str, UUID]
    name: str


user_01 = User(id=123, name='John Doe')
print(user_01)
# > id=123 name='John Doe'
print(user_01.id)
# > 123
user_02 = User(id='1234', name='John Doe')
print(user_02)
# > id=1234 name='John Doe'
print(user_02.id)
# > 1234
user_03_uuid = UUID('cf57432e-809e-4353-adbd-9d5c0d733868')
user_03 = User(id=user_03_uuid, name='John Doe')
print(user_03)
# > id=275603287559914445491632874575877060712 name='John Doe'
"""
However, as can be seen above, pydantic will attempt to 'match' any of the types defined under Union and will use the first one that matches. In the above example the id of user_03 was defined as a uuid.UUID class (which is defined under the attribute's Union annotation) but as the uuid.UUID can be marshalled into an int it chose to match against the int type and disregarded the other types.

As such, it is recommended that, when defining Union annotations, the most specific type is included first and followed by less specific types. In the above example, the UUID class should precede the int and str classes to preclude the unexpected representation as such:
"""
