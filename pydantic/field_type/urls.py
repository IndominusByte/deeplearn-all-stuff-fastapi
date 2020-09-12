"""
For URI/URL validation the following types are available:

- AnyUrl: any scheme allowed, TLD not required
- AnyHttpUrl: schema http or https, TLD not required
- HttpUrl: schema http or https, TLD required, max length 2083
- PostgresDsn: schema postgres or postgresql, user info required, TLD not required
- RedisDsn: schema redis, user info not required, tld not required (CHANGED: user info not required from v1.6 onwards)
- stricturl, method with the following keyword arguments:
    strip_whitespace: bool = True
    min_length: int = 1
    max_length: int = 2 ** 16
    tld_required: bool = True
    allowed_schemes: Optional[Set[str]] = None
    The above types (which all inherit from AnyUrl) will attempt to give descriptive errors when invalid URLs are provided:
"""
from pydantic import BaseModel, HttpUrl, ValidationError


class MyModel(BaseModel):
    url: HttpUrl


m = MyModel(url='http://www.example.com')
print(m.url)
# > http://www.example.com
try:
    MyModel(url='ftp://invalid.url')
except ValidationError as e:
    print(e.json())
    print()
    """
    1 validation error for MyModel
    url
      URL scheme not permitted (type=value_error.url.scheme;
    allowed_schemes={'http', 'https'})
    """

try:
    MyModel(url='not a url')
except ValidationError as e:
    print(e.json())
    """
    1 validation error for MyModel
    url
      invalid or missing URL scheme (type=value_error.url.scheme)
    """
