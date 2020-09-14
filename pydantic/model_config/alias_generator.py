# a callable that takes a field name and returns an alias for it
from pydantic import BaseModel


def to_camel(string: str) -> str:
    return ''.join(word.capitalize() for word in string.split('_'))

class Voice(BaseModel):
    name: str
    language_code: str

    class Config:
        """
        If data source field names do not match your code style (e. g. CamelCase fields),
        you can automatically generate aliases using alias_generator:
        """
        alias_generator = to_camel


voice = Voice(Name='Filiz', LanguageCode='tr-TR')
print(voice.language_code)
# > tr-TR
print(voice.dict(by_alias=True))
# > {'Name': 'Filiz', 'LanguageCode': 'tr-TR'}
