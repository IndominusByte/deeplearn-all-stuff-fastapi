"""
Serialisation can be customised on a model using the json_encoders config property; the keys should be types, and the values should be functions which serialise that type (see the example below):
"""
from pydantic import BaseModel
from datetime import datetime, timedelta
from pydantic.json import timedelta_isoformat

class WithCustomEncoders(BaseModel):
    dt: datetime
    diff: timedelta

    class Config:
        json_encoders = {
            datetime: lambda x: x.timestamp(),
            timedelta: timedelta_isoformat
        }


m = WithCustomEncoders(dt=datetime(2032, 6, 1), diff=timedelta(hours=100))
print(m.json())
# > {"dt": 1969660800.0, "diff": "P4DT4H0M0.000000S"}
