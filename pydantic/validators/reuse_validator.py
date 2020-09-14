"""
Occasionally, you will want to use the same validator on multiple fields/models (e.g. to normalize some input data). The "naive" approach would be to write a separate function, then call it from multiple decorators. Obviously, this entails a lot of repetition and boiler plate code. To circumvent this, the allow_reuse parameter has been added to pydantic.validator in v1.2 (False by default):
"""
from pydantic import BaseModel, validator

def normalize(name: str) -> str:
    return ' '.join([x.capitalize() for x in name.split(' ')])


class Producer(BaseModel):
    name: str

    # validators
    _normalize_name = validator('name', allow_reuse=True)(normalize)

class Consumer(BaseModel):
    name: str

    # validators
    _normalize_name = validator('name', allow_reuse=True)(normalize)


jane_doe = Producer(name='JaNe DOE')
john_doe = Consumer(name='joHN dOe')
assert jane_doe.name == 'Jane Doe'
assert john_doe.name == 'John Doe'
