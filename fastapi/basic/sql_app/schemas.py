from pydantic import BaseModel, EmailStr, SecretStr
from typing import List

# ========= ITEMS ===========
class Item(BaseModel):
    name: str

class ItemCreate(Item):
    class Config:
        min_anystr_length = 1
        max_anystr_length = 20
        anystr_strip_whitespace = True

class ItemOut(Item):
    id: int
    user_id: int

# ========== User ========
class User(BaseModel):
    username: str

class UserRegister(User):
    email: EmailStr
    password: SecretStr

    class Config:
        min_anystr_length = 1
        max_anystr_length = 100
        anystr_strip_whitespace = True

class UserUpdate(User):
    pass

class UserOut(User):
    email: EmailStr
    items: List[ItemOut]
