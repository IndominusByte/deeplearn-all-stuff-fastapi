from pydantic import BaseModel
from pydantic.types import constr, PaymentCardNumber, PaymentCardBrand
from datetime import date

class Card(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)
    number: PaymentCardNumber
    exp: date

    @property
    def brand(self) -> PaymentCardBrand:
        return self.number.brand

    @property
    def expired(self) -> bool:
        return self.exp < date.today()


card = Card(
    name='Georg Wilhelm Friedrich Hegel',
    number='4000000000000002',
    exp=date(2023, 9, 30),
)

"""
PaymentCardBrand can be one of the following based on the BIN:

- PaymentCardBrand.amex
- PaymentCardBrand.mastercard
- PaymentCardBrand.visa
- PaymentCardBrand.other
"""
assert card.number.brand == PaymentCardBrand.visa
assert card.number.bin == '400000'
assert card.number.last4 == '0002'
assert card.number.masked == '400000******0002'
