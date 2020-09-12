from pydantic import BaseModel
from typing import Callable

# Callable type; Callable[[int], str] is a function of (int) -> str.
"""
Callable fields only perform a simple check that the argument is callable;
no validation of arguments, their types, or the return type is performed.
"""
class Foo(BaseModel):
    callback: Callable[[int], int]


m = Foo(callback=lambda x: x)
print(m)
# > callback=<function <lambda> at 0x7f359366c280>
