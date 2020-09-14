"""
For performance reasons, by default validators are not called for fields when a value is not supplied. However there are situations where it may be useful or required to always call the validator, e.g. to set a dynamic default value.

You'll often want to use this together with pre, since otherwise with always=True pydantic would try to validate the default None which would cause an error.
"""
from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional

class DemoModel(BaseModel):
    ts: Optional[datetime] = None

    @validator('ts',always=True)
    def validate_ts(cls,v):
        return v or datetime.now()


print(DemoModel())
# > ts=datetime.datetime(2020, 7, 15, 20, 1, 48, 966302)
print(DemoModel(ts='2017-11-08T14:00'))
# > ts=datetime.datetime(2017, 11, 8, 14, 0)
