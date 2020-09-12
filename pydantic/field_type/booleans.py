"""
A standard bool field will raise a ValidationError if the value is not one of the following:

- A valid boolean (i.e. True or False),
- The integers 0 or 1,
- str which when converted to lower case is one of '0', 'off', 'f', 'false', 'n', 'no', '1', 'on', 't', 'true', 'y', 'yes'
- bytes which is valid (per the previous rule) when decoded to str

Note:
If you want stricter boolean logic (e.g. a field which only permits True and False) you can use StrictBool.
"""
from pydantic import BaseModel, ValidationError

class BooleanModel(BaseModel):
    bool_value: bool


print(BooleanModel(bool_value='true'))
# > bool_value=True
print(BooleanModel(bool_value='off'))
# > bool_value=False
try:
    BooleanModel(bool_value=[])
except ValidationError as e:
    print(str(e))
    """
    1 validation error for BooleanModel
    bool_value
      value could not be parsed to a boolean (type=type_error.bool)
    """
