# the min length for str & byte types (default: 0)
from pydantic import BaseModel, ValidationError

class Model(BaseModel):
    namestr: str
    bytestr: bytes

    class Config:
        min_anystr_length = 1


try:
    Model(namestr='',bytestr='')
except ValidationError as err:
    print(err)
    """
    2 validation errors for Model
    namestr
      ensure this value has at least 1 characters (type=value_error.any_str.min_length; limit_value=1)
    bytestr
      ensure this value has at least 1 characters (type=value_error.any_str.min_length; limit_value=1)
    """
