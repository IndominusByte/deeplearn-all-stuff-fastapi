"""
You can use the SecretStr and the SecretBytes data types for storing sensitive information that you do not want to be visible in logging or tracebacks. SecretStr and SecretBytes can be initialized idempotently or by using str or bytes literals respectively. The SecretStr and SecretBytes will be formatted as either '**********' or '' on conversion to json.
"""
from pydantic import BaseModel, SecretStr, SecretBytes, ValidationError

class SimpleModel(BaseModel):
    password: SecretStr
    password_bytes: SecretBytes


sm = SimpleModel(password='IAmSensitive',password_bytes=b'IAmSensitiveByte')
# Standard access methods will not display the secret
print(sm)
# > password=SecretStr('**********') password_bytes=SecretBytes(b'**********')
print(sm.password)
# > **********
print(sm.dict())
"""
{
    'password': SecretStr('**********'),
    'password_bytes': SecretBytes(b'**********'),
}
"""
print(sm.json())
# > {"password": "**********", "password_bytes": "**********"}
# Use get_secret_value method to see the secret's content.
print(sm.password.get_secret_value())
# > IAmSensitive
print(sm.password_bytes.get_secret_value())
# > b'IAmSensitiveBytes'

try:
    SimpleModel(password=[1, 2, 3], password_bytes=[1, 2, 3])
except ValidationError as e:
    print(e)
    """
    2 validation errors for SimpleModel
    password
      str type expected (type=type_error.str)
    password_bytes
      byte type expected (type=type_error.bytes)
    """

# If you want the secret to be dumped as plain-text using the json method,
# you can use json_encoders in the Config class.
class SimpleModelDumpable(BaseModel):
    password: SecretStr
    password_bytes: SecretBytes

    class Config:
        json_encoders = {
            SecretStr: lambda v: v.get_secret_value() if v else None,
            SecretBytes: lambda v: v.get_secret_value() if v else None,
        }


sm2 = SimpleModelDumpable(
    password='IAmSensitive', password_bytes=b'IAmSensitiveBytes'
)

# Standard access methods will not display the secret
print(sm2)
# > password=SecretStr('**********') password_bytes=SecretBytes(b'**********')
print(sm2.password)
# > **********
print(sm2.dict())
"""
{
    'password': SecretStr('**********'),
    'password_bytes': SecretBytes(b'**********'),
}
"""
# But the json method will
print(sm2.json())
# > {"password": "IAmSensitive", "password_bytes": "IAmSensitiveBytes"}
