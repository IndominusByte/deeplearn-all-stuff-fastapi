# the max length for str & byte types (default: 2 ** 16) = 65536
from pydantic import BaseModel, ValidationError

class Model(BaseModel):
    namestr: str
    bytename: bytes

    class Config:
        max_anystr_length = 10


try:
    Model(namestr='a' * 1000000,bytename='')
except ValidationError as err:
    print(err)
    """
    1 validation error for Model
    namestr
      ensure this value has at most 10 characters (type=value_error.any_str.max_length; limit_value=10)
    """
