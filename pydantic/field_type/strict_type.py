"""
You can use the StrictStr, StrictInt, StrictFloat, and StrictBool types to prevent coercion from compatible types. These types will only pass validation when the validated value is of the respective type or is a subtype of that type. This behavior is also exposed via the strict field of the ConstrainedStr, ConstrainedFloat and ConstrainedInt classes and can be combined with a multitude of complex validation rules.

The following caveats apply:

- StrictInt (and the strict option of ConstrainedInt) will not accept bool types,
    even though bool is a subclass of int in Python. Other subclasses will work.
- StrictFloat (and the strict option of ConstrainedFloat) will not accept int.
"""
from pydantic import BaseModel, StrictInt, ValidationError, confloat, StrictBool

class StrictIntModel(BaseModel):
    strict_int: StrictInt


try:
    StrictIntModel(strict_int=3.14159)
except ValidationError as e:
    print(e)
    """
    1 validation error for StrictIntModel
    strict_int
      value is not a valid integer (type=type_error.integer)
    """

class ConstrainedFloatModel(BaseModel):
    constrained_float: confloat(strict=True, ge=0.0)


try:
    ConstrainedFloatModel(constrained_float=3)
except ValidationError as e:
    print(e)
    """
    1 validation error for ConstrainedFloatModel
    constrained_float
      value is not a valid float (type=type_error.float)
    """

try:
    ConstrainedFloatModel(constrained_float=-1.23)
except ValidationError as e:
    print(e)
    """
    1 validation error for ConstrainedFloatModel
    constrained_float
      ensure this value is greater than or equal to 0.0
    (type=value_error.number.not_ge; limit_value=0.0)
    """

class StrictBoolModel(BaseModel):
    strict_bool: StrictBool


try:
    StrictBoolModel(strict_bool='False')
except ValidationError as e:
    print(str(e))
    """
    1 validation error for StrictBoolModel
    strict_bool
      value is not a valid boolean (type=value_error.strictbool)
    """
