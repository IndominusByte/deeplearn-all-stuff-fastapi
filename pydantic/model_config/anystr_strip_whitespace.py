# whether to strip leading and trailing whitespace for str & byte types (default: False)
from pydantic import BaseModel

class Model(BaseModel):
    namestr: str
    bytestr: bytes

    class Config:
        anystr_strip_whitespace = True


m = Model(namestr='asd      ',bytestr=b'asd            ')
print(m)
# > namestr='asd' bytestr=b'asd'
