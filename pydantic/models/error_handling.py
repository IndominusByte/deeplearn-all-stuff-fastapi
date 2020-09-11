from pydantic import BaseModel, conint, confloat, ValidationError
from typing import Optional, List

class Location(BaseModel):
    lat: Optional[float] = 0.1
    lng: Optional[float] = 10.1

class Model(BaseModel):
    is_required: confloat(gt=10)
    gt_int: conint(gt=42)
    list_of_ints: List[int] = None
    a_float: Optional[float] = None
    recursive_model: Optional[Location] = None


data = dict(
    is_required=11,
    list_of_ints=['1', 2, 'bad'],
    a_float='not a float',
    recursive_model={'lat': 4.2, 'lng': 'New York'},
    gt_int=43.22,
)

try:
    Model(**data)
except ValidationError as e:
    # method will return a human readable representation of the errors.
    print(e)
    print()
    # method will return a JSON representation of errors.
    print(e.json())
    print()
    # method will return list of errors found in the input data.
    print(e.errors())
