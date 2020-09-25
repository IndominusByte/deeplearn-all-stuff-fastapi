from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, SecretStr
from typing import Optional, List

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []

    class Config:
        min_anystr_length = 1
        anystr_strip_whitespace = True


app = FastAPI()

"""
The response model is declared in this parameter instead of as a function return type annotation, because the path function may not actually return that response model but rather return a dict, database object or some other model, and then use the response_model to perform the field limiting and serialization.
"""
@app.post('/items', response_model=Item)
def create_items(item: Item):
    return item

# best practice
class UserIn(BaseModel):
    username: str
    password: SecretStr
    email: EmailStr
    fullname: Optional[str] = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    fullname: Optional[str] = None


# @app.post('/user', response_model=UserOut)
# def create_user(user: UserIn):
#     return user

"""
You can set the path operation decorator parameter response_model_exclude_unset=True
and those default values won't be included in the response, only the values actually set.

You can also use:

- response_model_exclude_defaults=True
- response_model_exclude_none=True
"""
# @app.post('/user', response_model=UserOut, response_model_exclude_unset=True)
# def create_user(user: UserIn):
#     return user


"""
You can also use the path operation decorator parameters response_model_include and response_model_exclude. like pydantic except you should add response_model at beginning
"""
# @app.post('/user', response_model=UserOut, response_model_include={'username','email'})
# def create_user(user: UserIn):
#     return user

@app.post('/user', response_model=UserOut, response_model_exclude={'username','email'})
def create_user(user: UserIn):
    return user
