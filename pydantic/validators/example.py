"""
you can also add any subset of the following arguments to the signature (the names must match):
- values: a dict containing the name-to-value mapping of any previously-validated fields
- config: the model config
- field: the field being validated
- **kwargs: if provided, this will include the arguments above not explicitly listed in the signature
"""
from pydantic import BaseModel, validator, ValidationError
from pydantic.types import constr

class UserModel(BaseModel):
    name: str
    username: str
    password: constr(strict=True,strip_whitespace=True,min_length=1)
    password_confirm: constr(strict=True,strip_whitespace=True,min_length=1)

    @validator('name')
    def validate_name(cls, v):
        if ' ' not in v:
            raise ValueError('must contain a space')
        # Make the first letter in each word upper case
        return v.title()

    @validator('password_confirm')
    def validate_password_confirm(cls, v, values, **kwargs):
        """
        # if @validator('username') values is -> {'name': 'Samuel Colvin'}
        # Note: values: a dict containing the name-to-value mapping of any previously-validated fields

        values ->  {'name': 'Samuel Colvin', 'username': 'scolvin', 'password': 'zxcvbn'}

        kwargs -> {
            'field': ModelField(name='password_confirm', type=str, required=True),
            'config': <class '__main__.Config'>
        }
        """
        if 'password' in values and v != values['password']:
            raise ValueError('passwords do not match')
        return v

    @validator('username')
    def validate_username(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v


user = UserModel(
    name='samuel colvin',
    username='scolvin12',
    password='zxcvbn',
    password_confirm='zxcvbn',
)
print(user)
print()
# name='Samuel Colvin' username='scolvin12' password='zxcvbn' password_confirm='zxcvbn'

try:
    UserModel(
        name='samuel',
        username='scolvin!@#',
        password='zxcvbn',
        password_confirm='zxcvbn2',
    )
except ValidationError as e:
    print(e)
    """
    3 validation errors for UserModel
    name
      must contain a space (type=value_error)
    username
      must be alphanumeric (type=assertion_error)
    password_confirm
      passwords do not match (type=value_error)
    """
