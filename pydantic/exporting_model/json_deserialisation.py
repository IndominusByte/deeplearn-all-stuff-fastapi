"""
To improve the performance of encoding and decoding JSON, alternative JSON implementations (e.g. ujson) can be used via the json_loads and json_dumps properties of Config.
"""
import ujson, orjson
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class User(BaseModel):
    id: int
    name: Optional[str] = 'John Doe'
    signup_ts: Optional[datetime] = None

    class Config:
        json_loads = ujson.loads


user = User.parse_raw('{"id": 123,"signup_ts":1234567890,"name":"John Doe"}')
print(user.json())

"""
ujson generally cannot be used to dump JSON since it doesn't support encoding of objects like datetimes and does not accept a default fallback function argument. To do this, you may use another library like orjson.

Note: that orjson takes care of datetime encoding natively, making it faster than json.dumps but meaning you cannot always customise the encoding using Config.json_encoders.
"""
def orjson_dumps(v,*,default):
    return orjson.dumps(v, default=default).decode()

class User2(BaseModel):
    id: int
    name: Optional[str] = 'John Doe'
    signup_ts: Optional[datetime] = None

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


user2 = User2.parse_raw('{"id": 123,"signup_ts":1234567890,"name":"John Doe"}')
print(user2.json())
