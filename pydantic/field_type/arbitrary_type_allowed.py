from pydantic import BaseModel, ValidationError

# This is not a pydantic model, it's an arbitrary class
class Pet:
    def __init__(self, name: str):
        self.name = name


class Model(BaseModel):
    pet: Pet
    owner: str

    class Config:
        arbitrary_types_allowed = True


pet = Pet(name='Hedwig')
# A simple check of instance type is used to validate the data
model = Model(owner='Harry', pet=pet)
print(model)
# > pet=<__main__.Pet object at 0x7ff700d2b070> owner='Harry'
print(model.pet)
# > <__main__.Pet object at 0x7fba0ce39070>
print(model.pet.name)
# > Hedwig
print(type(model.pet))
# > <class '__main__.Pet'>
try:
    # If the value is not an instance of the type, it's invalid
    Model(owner='Harry', pet='Hedwig')
except ValidationError as e:
    print(e)
    """
    1 validation error for Model
    pet
      instance of Pet expected (type=type_error.arbitrary_type;
    expected_arbitrary_type=Pet)
    """

# Nothing in the instance of the arbitrary type is checked
# Here name probably should have been a str, but it's not validated
pet2 = Pet(name=42)
model2 = Model(owner='Harry', pet=pet2)
print(model2)
# > pet=<__main__.Pet object at 0x7fdc974dc0d0> owner='Harry'
print(model2.pet)
# > <__main__.Pet object at 0x7fe1e88ce0d0>
print(model2.pet.name)
# > 42
