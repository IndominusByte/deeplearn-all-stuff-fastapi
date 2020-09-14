"""
If using a validator with a subclass that references a List type field on a parent class, using each_item=True will cause the validator not to run; instead, the list must be iterated over programatically.
"""
from typing import List
from pydantic import BaseModel, ValidationError, validator


class ParentModel(BaseModel):
    names: List[str]


class ChildModel(ParentModel):
    @validator('names', each_item=True)
    def check_names_not_empty(cls, v):
        assert v != '', 'Empty strings are not allowed.'
        return v


# This will NOT raise a ValidationError because the validator was not called
try:
    child = ChildModel(names=['Alice', 'Bob', 'Eve', ''])
except ValidationError as e:
    print(e)
else:
    print('No ValidationError caught.')
    # > No ValidationError caught.


class ChildModel2(ParentModel):
    @validator('names')
    def check_names_not_empty(cls, v):
        for name in v:
            assert name != '', 'Empty strings are not allowed.'
        return v


try:
    child = ChildModel2(names=['Alice', 'Bob', 'Eve', ''])
except ValidationError as e:
    print(e)
    """
    1 validation error for ChildModel2
    names
      Empty strings are not allowed. (type=assertion_error)
    """
