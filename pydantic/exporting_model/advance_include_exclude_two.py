"""
Special care must be taken when including or excluding fields from a list or tuple of submodels or dictionaries. In this scenario, dict and related methods expect integer keys for element-wise inclusion or exclusion. To exclude a field from every member of a list or tuple, the dictionary key '__all__' can be used as follows:
"""
import datetime
from pydantic import BaseModel, SecretStr
from typing import List

class Country(BaseModel):
    name: str
    phone_code: int

class Address(BaseModel):
    post_code: int
    country: Country

class CardDetails(BaseModel):
    number: SecretStr
    expires: datetime.date

class Hobby(BaseModel):
    name: str
    info: str

class User(BaseModel):
    first_name: str
    second_name: str
    address: Address
    card_details: CardDetails
    hobbies: List[Hobby]


user = User(
    first_name='John',
    second_name='Doe',
    address=Address(
        post_code=123456,
        country=Country(
            name='USA',
            phone_code=1
        )
    ),
    card_details=CardDetails(
        number=4212934504460000,
        expires=datetime.date(2020, 5, 1)
    ),
    hobbies=[
        Hobby(name='Programming', info='Writing code and stuff'),
        Hobby(name='Gaming', info='Hell Yeah!!!'),
    ],
)

exclude_keys = {
    'second_name': ...,
    'address': {'post_code': ..., 'country': {'phone_code'}},
    'card_details': ...,
    # You can exclude fields from specific members of a tuple/list by index:
    'hobbies': {-1: {'info'}},
}

include_keys = {
    'first_name': ...,
    'address': {'country': {'name'}},
    'hobbies': {0: ..., -1: {'name'}},
}

# would be the same as user.dict(exclude=exclude_keys) in this case:
print(user.dict(include=include_keys))
"""
{
    'first_name': 'John',
    'address': {'country': {'name': 'USA'}},
    'hobbies': [
        {
            'name': 'Programming',
            'info': 'Writing code and stuff',
        },
        {'name': 'Gaming'},
    ],
}
"""
# To exclude a field from all members of a nested list or tuple, use "__all__":
print(user.dict(exclude={'hobbies': {'__all__': {'info'}}}))
"""
{
    'first_name': 'John',
    'second_name': 'Doe',
    'address': {
        'post_code': 123456,
        'country': {'name': 'USA', 'phone_code': 1},
    },
    'card_details': {
        'number': SecretStr('**********'),
        'expires': datetime.date(2020, 5, 1),
    },
    'hobbies': [{'name': 'Programming'}, {'name': 'Gaming'}],
}
"""
