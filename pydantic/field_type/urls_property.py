# URL Properties
"""
Assuming an input URL of http://samuel:pass@example.com:8000/the/path/?query=here#fragment=is;this=bit,
the above types export the following properties:

- scheme: always set - the url schema (http above)
- host: always set - the url host (example.com above)
- host_type: always set - describes the type of host, either:
- domain: e.g. example.com,
- int_domain: international domain, see below, e.g. exampl£e.org,
- ipv4: an IP V4 address, e.g. 127.0.0.1, or
- ipv6: an IP V6 address, e.g. 2001:db8:ff00:42
- user: optional - the username if included (samuel above)
- password: optional - the password if included (pass above)
- tld: optional - the top level domain (com above), Note: this will be wrong for any two-level domain,
    e.g. "co.uk". You'll need to implement your own list of TLDs if you require full TLD validation
- port: optional - the port (8000 above)
- path: optional - the path (/the/path/ above)
- query: optional - the URL query (aka GET arguments or "search string") (query=here above)
- fragment: optional - the fragment (fragment=is;this=bit above)
"""
from pydantic import BaseModel, HttpUrl, PostgresDsn, validator, ValidationError

class Model(BaseModel):
    url: HttpUrl


m = Model(url='http://www.example.com')
print(m)
# > url=HttpUrl('http://www.example.com', scheme='http', host='www.example.com', tld='com', host_type='domain')
print(m.url.scheme)
# > http
print(m.url.host)
# > www.example.com
print(m.url.tld)
# > com
print(m.url.port)
# > None

class DatabaseModel(BaseModel):
    db: PostgresDsn

    @validator('db')
    def validate_db(cls, value):
        assert value.path and len(value.path) > 1, 'database must be provided'
        return value


m = DatabaseModel(db='postgres://user:pass@localhost:5432/foobar')
print(m.db)
# > postgres://user:pass@localhost:5432/foobar

try:
    DatabaseModel(db='postgres://user:pass@localhost:5432/')
except ValidationError as e:
    print(e)
    """
    1 validation error for DatabaseModel
    db
        database must be provided (type=assertion_error)
    """
