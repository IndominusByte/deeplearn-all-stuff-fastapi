"""
If you have a generator you can use Sequence as described above. In that case,
the generator will be consumed and stored on the model as a list and its values will be validated
with the sub-type of Sequence (e.g. int in Sequence[int]).

But if you have a generator that you don't want to be consumed,
e.g. an infinite generator or a remote data loader, you can define its type with Iterable:
"""
from pydantic import BaseModel, validator, ValidationError
from pydantic.fields import ModelField
from typing import Iterable

class Model(BaseModel):
    infinite: Iterable[int]

    @validator('infinite')
    # You don't need to add the "ModelField", but it will help your
    # editor give you completion and catch errors
    def test(cls, value, field: ModelField):
        first_value = next(value)
        if (sub_field := field.sub_fields):
            # The Iterable had a parameter type, in this case it's int
            # We use it to validate the first value
            v, error = sub_field[0].validate(first_value, {}, loc='first_value')
            if error:
                raise ValidationError([error],cls)
        return value


def infinite_ints():
    i = 0
    while True:
        yield i
        i += 1


m = Model(infinite=infinite_ints())
print(m)
# > infinite=<generator object infinite_ints at 0x7f35939f4f90>
for i in m.infinite:
    print(i)
    if i == 10:
        break

def infinite_strs():
    for letter in 'allthesingleladies':
        yield letter


try:
    Model(infinite=infinite_strs())
except ValidationError as e:
    print(e)
    """
    1 validation error for Model
    infinite -> first_value
      value is not a valid integer (type=type_error.integer)
    """
