"""
Type[T] to specify that a field may only accept classes (not instances) that are subclasses of T.

class User: ...
class BasicUser(User): ...
class ProUser(User): ...
class TeamUser(User): ...

# Accepts User, BasicUser, ProUser, TeamUser, ...
def make_new_user(user_class: Type[User]) -> User:
    # ...
    return user_class()
"""
from pydantic import BaseModel, ValidationError
from typing import Type

class Foo:
    pass


class Bar(Foo):
    pass


class Other:
    pass


class SimpleModel(BaseModel):
    just_subclasses: Type[Foo]


SimpleModel(just_subclasses=Foo)
SimpleModel(just_subclasses=Bar)
try:
    SimpleModel(just_subclasses=Other)
except ValidationError as e:
    print(e)
    """
    1 validation error for SimpleModel
    just_subclasses
      subclass of Foo expected (type=type_error.subclass; expected_class=Foo)
    """
