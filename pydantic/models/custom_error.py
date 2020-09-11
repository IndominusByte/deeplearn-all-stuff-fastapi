from pydantic import BaseModel, validator, ValidationError, PydanticValueError

"""
Validation code should not raise ValidationError itself, but rather raise ValueError,
TypeError or AssertionError (or subclasses of ValueError or TypeError) which will be caught
and used to populate ValidationError.
"""
class Model(BaseModel):
    foo: str

    @validator('foo')
    def validate_foo(cls, v):
        if v != 'bar':
            # raise Exception('This is the exception you expect to handle')
            raise ValueError("value must be 'bar'")

        return v


try:
    Model(foo='ber')
except ValidationError as e:
    print(e.json())

"""
You can also define your own error classes, which can specify a custom error code, message template, and context:
"""
class NotABarError(PydanticValueError):
    code: str = 'not_a_bar'
    msg_template: str = 'value is not "bar", got "{wrong_value}"'

class Model2(BaseModel):
    foo: str

    @validator('foo')
    def name_must_contain_space(cls, v):
        if v != 'bar':
            raise NotABarError(wrong_value=v)
        return v


try:
    Model2(foo='ber')
except ValidationError as e:
    print(e.json())
