"""
Validation can also be performed on the entire model's data.

As with field validators, root validators can have pre=True, in which case they're called before field validation occurs

Field validation will not occur if pre=True root validators raise an error. As with field validators, "post" (i.e. pre=False) root validators by default will be called even if prior validators fail; this behaviour can be changed by setting the skip_on_failure=True keyword argument to the validator. The values argument will be a dict containing the values which passed field validation and field defaults where applicable.
"""
from pydantic import BaseModel, root_validator, ValidationError
from pydantic.types import constr

class UserModel(BaseModel):
    username: str
    password1: constr(strict=True,strip_whitespace=True,min_length=1)
    password2: constr(strict=True,strip_whitespace=True,min_length=1)

    @root_validator(pre=True)
    def check_card_number_omitted(cls, values):
        assert 'card_number' not in values, 'card_number should not be included'
        return values

    @root_validator
    def check_passwords_match(cls, values):
        p1, p2 = values.get('password1'), values.get('password2')
        if (p1 and p2) and p1 != p2:
            raise ValueError('passwords do not match')
        return values


print(UserModel(username='scolvin', password1='zxcvbn', password2='zxcvbn'))
# > username='scolvin' password1='zxcvbn' password2='zxcvbn'

try:
    UserModel(username='scolvin', password1='zxcvbn', password2='zxcvbn2')
except ValidationError as e:
    print(e)
    """
    1 validation error for UserModel
    __root__
      passwords do not match (type=value_error)
    """

try:
    UserModel(
        username='scolvin',
        password1='zxcvbn',
        password2='zxcvbn',
        card_number='1234',
    )
except ValidationError as e:
    print(e)
    """
    1 validation error for UserModel
    __root__
      card_number should not be included (type=assertion_error)
    """
