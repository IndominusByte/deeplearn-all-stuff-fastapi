"""
pydantic supports the use of typing.Literal (or typing_extensions.Literal prior to python 3.8)
as a lightweight way to specify that a field may accept only specific literal values:

A type that can be used to indicate to type checkers that the corresponding variable or function parameter has a value equivalent to the provided literal (or one of several literals). For example:

def validate_simple(data: Any) -> Literal[True]:  # always returns True
    ...

MODE = Literal['r', 'rb', 'w', 'wb']
def open_helper(file: str, mode: MODE) -> str:
    ...

open_helper('/some/path', 'r')  # Passes type check
open_helper('/other/path', 'typo')  # Error in type checker
"""
from typing import Literal
from pydantic import BaseModel, ValidationError

class Pie(BaseModel):
    flavor: Literal['apple', 'pumpkin']


Pie(flavor='apple')
Pie(flavor='pumpkin')
try:
    Pie(flavor='cherry')
except ValidationError as e:
    print(str(e))
    """
    1 validation error for Pie
    flavor
      unexpected value; permitted: 'apple', 'pumpkin'
    (type=value_error.const; given=cherry; permitted=('apple', 'pumpkin'))
    """
