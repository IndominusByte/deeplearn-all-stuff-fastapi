from pydantic import BaseModel, Field
from datetime import datetime
from uuid import uuid4, UUID
from typing import Optional

"""
To declare a field as required, you may declare it using just an annotation,
or you may use an ellipsis (...) as the value:
"""
class Model(BaseModel):
    a: Optional[int] = None
    b: Optional[int] = ...
    c: int = Field(...)


print(Model(b=1, c=2))

# Field with dynamic default value
# Note: still beta
class Model2(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    updated: datetime = Field(default_factory=datetime.utcnow)


m = Model2()
print(m)
