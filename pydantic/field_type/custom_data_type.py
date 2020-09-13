from pydantic import BaseModel, ValidationError

"""
You use a custom class with a classmethod __get_validators__
It will be called to get validators to parse and validate the input data.
"""
class NoHandphone:
    @classmethod
    def __get_validators__(cls):
        # one or more validators may be yielded which will be called in the
        # order to validate the input, each validator will receive as an input
        # the value returned from the previous validator
        yield cls.validate
        yield cls.validate_my_number

    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise TypeError('string required')

        if v[:2] != '08':
            raise ValueError('not valid handphone +62')
        return v

    @classmethod
    def validate_my_number(cls, v):
        if v != '0818181':
            raise ValueError('this is not my number')
        return v


class Model(BaseModel):
    no_hp: NoHandphone


try:
    m = Model(no_hp='0818181')
    print(m)
except ValidationError as err:
    print(err.json())
